import json

# Define input json file and target jsonl file
input_file_path = "./data/faq_dataset.json"
output_file_path = "./data/faq_dataset_converted.jsonl"

def convert_json_to_chat(input_file, output_file):

    try:
        # Load the questions and answers from the input JSON file
        with open(input_file, 'r') as file:
            data = json.load(file)
        
        with open(output_file, 'w') as file:
            # Iterate over each question and answer pair and write the chat format to the output file
            for item in data:
                chat_format = {
                    "messages": [
                        {"role": "user", "content": item.get("question")},
                        {"role": "assistant", "content": item.get("answer")}
                    ]
                }

                # Write the chat conversation as a json line in the output file
                file.write(json.dumps(chat_format) + '\n')

        print(f"The dataset from {input_file} was successfully converted to {output_file}")
    except Exception as e:
        
        print(f"An error occured: {e}")
        

# Call the function to perform the conversion
convert_json_to_chat(input_file_path, output_file_path)

    
   



