import os 
import dotenv 
from openai import OpenAI

dotenv.load_dotenv()

try:

    # Load API key from environment variable
    client = OpenAI(api_key = os.getenv('OPENAI_APIKEY'))

    # Upload training and validation data to openai for finetuning
    training_dataset = client.files.create(
        file = open("../data/training.jsonl", "rb"),
        purpose = "fine-tune"
    )

    validation_dataset = client.files.create(
        file = open("../data/validation.jsonl", "rb"),
        purpose = "fine-tune"
    )

    # Print file objects
    print("Files were successfully uploaded to openai")
    print("-----------------------------")
    print(training_dataset)
    print("-----------------------------")
    print(validation_dataset)

except Exception as e:

    print(f"An error occured: {e}")

