from src.utils import create_fine_tuning
import os
import time
import openai
import pandas as pd
import dotenv
import matplotlib.pyplot as plt

dotenv.load_dotenv()

model_name = 'gpt-3.5-turbo'
openai_key = os.getenv('OPENAI_APIKEY')
train_file_id = os.getenv('TRAIN_FILE_ID')
evaluation_file_id = os.getenv('EVAL_FILE_ID')

# Start fine-tuning job
fine_tuning_response = create_fine_tuning(model_name, openai_key, train_file_id, evaluation_file_id)
print(fine_tuning_response)

fine_tuning_job_ID = fine_tuning_response['id']
df = pd.DataFrame(columns=["Step", "Train Loss", "Train Accuracy", "Validation Loss", "Validation Accuracy"])

while True:
    job = openai.fine_tuning.jobs.list_events(id=fine_tuning_job_ID, limit=1)
    if not job.data:
        print("No job data available; waiting...")
        time.sleep(30)
        continue

    latest_event = job.data[0]
    if latest_event["message"] == "Fine-tuning job successfully completed":
        print("Fine-tuning completed.")
        break

    if "data" in latest_event:
        step = latest_event["data"]["step"]
        train_loss = latest_event["data"]["train_loss"]
        train_accuracy = latest_event["data"]["train_mean_token_accuracy"]
        eval_loss = latest_event["data"]["valid_loss"]
        eval_accuracy = latest_event["data"]["valid_mean_token_accuracy"]

        # Update DataFrame
        new_data = {
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
        plt.draw()
        plt.pause(1)
        plt.clf()

    time.sleep(30)
