import json 
import os 
from sklearn.model_selection import train_test_split 

def split_data(input_file, train_output_path, val_output_path):
    """
    Splits a JSONL file into training and validation sets using sklearn's train_test_split
    and saves them to the specified paths.

    Args:
        input_file (str): Path to the input JSONL file.
        train_output_path (str): Path to save the training JSONL file.
        val_output_path (str): Path to save the validation JSONL file.
    """
    try:
     
        # Load data from JSONL file
        with open(input_file, 'r') as f:
            data = [json.loads(line) for line in f]

        # Split data into training and validation set
        train_set, val_set = train_test_split(data, train_size=0.8, random_state=42)

        # Save training and validation data
        with open(train_output_path, 'w') as f_train:
            for record in train_set:
                    f_train.write(json.dumps(record) + '\n')

        with open(val_output_path, 'w') as f_val:
            for record in val_set:
                    f_val.write(json.dumps(record) + '\n')

        print(f"Training data saved to {train_output_path}")
        print(f"Validation data saved to {val_output_path}")

    except Exception as e:
      
        print(f"An error occured: {e}")

input_file = './data/faq_dataset_converted.jsonl'
train_output_path = './data/training.jsonl'
val_output_path = './data/validation.jsonl'

split_data(input_file, train_output_path, val_output_path)


      
      


        
              




    




    
