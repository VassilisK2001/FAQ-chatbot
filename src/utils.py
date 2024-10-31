from openai import OpenAI
import dotenv

dotenv.load_dotenv()

# Helper function for creating finetuning job
def create_fine_tuning(model_name, openai_key, train_id, eval_id, hyperparameters=None):
    client = OpenAI(api_key = openai_key)

    args = {
        "model": model_name,
        "training_file": train_id,
        "validation_file": eval_id
    }

    # Check if hyperparameters argument provided and ensure it's a dictionary
    if (hyperparameters is not None):
        if (isinstance(hyperparameters, dict)):
            args["hyperparameters"] = hyperparameters
        else:
            raise TypeError("hyperparameters must be a dictionary if provided")

    fine_tuning_response = client.fine_tuning.jobs.create(**args)

    return fine_tuning_response