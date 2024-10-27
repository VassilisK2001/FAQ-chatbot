from openai import OpenAI
import os 
import dotenv

dotenv.load_dotenv()

# Helper function for creating finetuning job
def create_fine_tuning(model_name, openai_key, train_id, eval_id):
    client = OpenAI(api_key = openai_key)

    fine_tuning_response = client.fine_tuning.jobs.create(
        model = model_name,
        training_file = train_id,
        validation_file = eval_id
    )

    return fine_tuning_response