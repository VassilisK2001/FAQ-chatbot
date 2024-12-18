from src.utils import get_model_response
import json
import os 
import dotenv 

dotenv.load_dotenv() 

# Retrive openai api key and fine-tuned model ID
api_key = os.getenv("OPENAI_APIKEY")
fine_tuned_model_ID = os.getenv("FINE_TUNED_MODEL_ID")

try:

    # Load test questions from test.json
    with open("test.json", "r") as f:
        test_data = json.load(f)


    # Process each question in the test data
    for item in test_data:
        question = item.get("question")
        if question:
            # Get model response
            model_output = get_model_response(api_key, fine_tuned_model_ID, question)
            
            # Add the response and model ID to dictionary
            response_data = {
                "fine_tuned_model_ID": fine_tuned_model_ID,
                "model_output": model_output
            }

            # Check if 'response_data' exists in items
            if ("response_data") in item:
                # If it exists, append response_data to the existing list
                item["response_data"].append(response_data)
            else:
                # If it doesn't exist, create response_data as a list with response_data as first item
                item["response_data"] = [response_data]


    # Overwrite the test.json with updated data
    with open("test.json", "w") as f:
        json.dump(test_data, f, indent=4)

    print("Model responses successfully added to test.json")

except Exception as e:

    print(f"An error occured: {e}")




