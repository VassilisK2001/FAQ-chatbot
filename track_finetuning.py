from src.utils import create_fine_tuning
import os
import time 
import openai 
import pandas as pd
import dotenv 
import matplotlib.pyplot as plt 
from termcolor import colored 

dotenv.load_dotenv()

model_name = 'gpt-3.5-turbo'
openai_key = os.getenv('OPENAI_APIKEY')
train_file_id = os.getenv('TRAIN_FILE_ID')
evaluation_file_id = os.getenv('EVAL_FILE_ID')

fine_tuning_response = create_fine_tuning(model_name, openai_key, train_file_id, evaluation_file_id) 
print(fine_tuning_response + '\n')

fine_tuning_job_ID = fine_tuning_response['id']

df = pd.DataFrame(columns=["Step", "Train Loss", "Train Accuracy", "Validation Loss", "Validation Accuracy"])
job_id = fine_tuning_job_ID 


