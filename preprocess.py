import re

def clean_and_format(raw_data_file):
    with open(raw_data_file, 'r') as file:
        lines = file.readlines()
    
    cleaned_data = []
    for line in lines:
        question, answer = line.split('+++')
        question = re.sub(r'\s+', ' ', question).strip()  # Remove extra whitespaces
        answer = re.sub(r'\s+', ' ', answer).strip()      # Remove extra whitespaces
        cleaned_data.append((question, answer))
    
    return cleaned_data

if __name__ == "__main__":
    raw_data_file = 'raw_data.txt'
    cleaned_data = clean_and_format(raw_data_file)
    
    # Save cleaned data for final processing
    with open('cleaned_data.txt', 'w') as file:
        for question, answer in cleaned_data:
            file.write(f"{question}+++{answer}\n")
