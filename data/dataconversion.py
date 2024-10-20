import json

input_file_path = "./data/shuffled_faq_dataset.json"
output_file_path = "./data/faq_dataset_converted.jsonl"

def convert_json_to_chat(input_file, output_file):
    # Load the questions and answers from the input JSON file
    with open(input_file, 'r') as file:
        data = json.load(file)
    
   



