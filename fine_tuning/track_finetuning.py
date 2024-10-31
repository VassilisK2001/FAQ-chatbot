from src.utils import create_fine_tuning
import os
import json
import time
import openai
import pandas as pd
import dotenv
import matplotlib.pyplot as plt
import logging

dotenv.load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

model_name = 'gpt-3.5-turbo'
openai_key = os.getenv('OPENAI_APIKEY')
train_file_id = os.getenv('TRAIN_FILE_ID')
evaluation_file_id = os.getenv('EVAL_FILE_ID')

# Start fine-tuning job
logging.info("Starting fine-tuning job.")
fine_tuning_response = create_fine_tuning(model_name, openai_key, train_file_id, evaluation_file_id)
logging.info("Fine-tuning job started successfully.")

fine_tuning_job_ID = fine_tuning_response['id']

# Initialize empty DataFrame with an additional column for the Fine-tuning Job ID
df = pd.DataFrame(columns=["Fine-tuning Job ID", "Step", "Train Loss", "Train Accuracy", "Validation Loss", "Validation Accuracy"])

# Define variables for full validation metrics
full_valid_loss = None 
full_valid_accuracy = None 

while True:
    logging.info("Polling for latest event from fine-tuning job.")
    # Poll for latest event from fine-tuning job
    job = openai.FineTuningJob.list_events(id=fine_tuning_job_ID, limit=1)
    
    if not job.data:
        logging.info("No job data available; waiting...\n")
        time.sleep(5)
        continue

    latest_event = job.data[0]

    if latest_event["message"] == "Fine-tuning job successfully completed":
        logging.info("Fine-tuning completed.\n")

        # If full validation metrics are in the last event, extract them here
        if "full_valid_loss" in latest_event["data"]:
            full_valid_loss = latest_event["data"]["full_valid_loss"]
            full_valid_accuracy = latest_event["data"]["full_valid_mean_token_accuracy"]
            
        break
    
    # Process and log intermediate training metrics if available
    if "data" in latest_event:
        step = latest_event["data"]["step"]
        train_loss = latest_event["data"]["train_loss"]
        train_accuracy = latest_event["data"]["train_mean_token_accuracy"]
        eval_loss = latest_event["data"]["valid_loss"]
        eval_accuracy = latest_event["data"]["valid_mean_token_accuracy"]

        # Update DataFrame with new data
        new_data = {
            "Fine-tuning Job ID": fine_tuning_job_ID,
            "Step": step,
            "Train Loss": train_loss,
            "Train Accuracy": train_accuracy,
            "Validation Loss": eval_loss,
            "Validation Accuracy": eval_accuracy,
        }
        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)

        # Save progress to CSV
        df.to_csv("finetuning_progress.csv", index=False)

        # Plotting
        logging.info("Generating plots for fine-tuning metrics.")
        plt.figure(figsize=(12, 6))

        plt.subplot(2, 2, 1)
        plt.plot(df["Step"], df["Train Loss"], label="Train Loss", color="blue")
        plt.xlabel("Steps")
        plt.ylabel("Train Loss")
        plt.legend()

        plt.subplot(2, 2, 2)
        plt.plot(df["Step"], df["Train Accuracy"], label="Train Accuracy", color="green")
        plt.xlabel("Steps")
        plt.ylabel("Train Accuracy")
        plt.legend()

        plt.subplot(2, 2, 3)
        plt.plot(df["Step"], df["Validation Loss"], label="Validation Loss", color="blue")
        plt.xlabel("Steps")
        plt.ylabel("Validation Loss")
        plt.legend()

        plt.subplot(2, 2, 4)
        plt.plot(df["Step"], df["Validation Accuracy"], label="Validation Accuracy", color="green")
        plt.xlabel("Steps")
        plt.ylabel("Validation Accuracy")
        plt.legend()

        plt.tight_layout()

        # Create a directory for models if it doesn't exist
        models_dir = "../models"
        if not os.path.exists(models_dir):
            os.makedirs(models_dir)

        # Save the plot as PNG; filename will be set after retrieving the fine-tuned model
        plt.savefig(os.path.join(models_dir, "temp_plot.png"))  # Temporarily save the plot
        plt.close()  # Close the figure to free memory

    time.sleep(30)

# Retrieve fine-tuned model and hyperparameters once the job is completed
logging.info("Retrieving fine-tuned model and hyperparameters.")
ft_retrieve = openai.FineTuningJob.retrieve(id=fine_tuning_job_ID)

# Response
logging.info("Fine-tuned model retrieved successfully.")
print(ft_retrieve, '\n')

model_id = ft_retrieve['fine_tuned_model']
hyperparameters = ft_retrieve.get('hyperparameters')

# Update plot filename with fine-tuned model ID
final_plot_filename = os.path.join(models_dir, f"{model_id}.png")
os.rename(os.path.join(models_dir, "temp_plot.png"), final_plot_filename)  # Rename the temporary plot file

# Define the dictionary with model info to add to models.json
model_info = {
    "model_id": model_id,
    "hyperparameters": hyperparameters,
    "full_validation_metrics": {
        "full_validation_loss": full_valid_loss,
        "full_validation_accuracy": full_valid_accuracy
    }   
}

# Load models.json, append new model info, and save 
models_path = "../models/models.json"
try:
    # Try loading existing data or create a new list if the file doesn't exist
    try:
        with open(models_path, 'r') as f:
            models_data = json.load(f)
    except FileNotFoundError:
        models_data = []

    # Append the new model info to the JSON file
    models_data.append(model_info)

    # Save updated data back to the JSON file
    with open(models_path, 'w') as f:
        json.dump(models_data, f, indent=4)

    logging.info("Model information saved to models.json\n")

except Exception as e:
    logging.error(f"An error occurred: {e}")
