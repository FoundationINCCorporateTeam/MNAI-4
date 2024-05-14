def save_to_file(cleaned_data_file, output_file):
    with open(cleaned_data_file, 'r') as file:
        lines = file.readlines()
    
    with open(output_file, 'w') as file:
        for idx, line in enumerate(lines, start=1):
            question, answer = line.split('+++')
            file.write(f"L{idx} +++$+++ general +++$+++ {question.strip()} +++$+++ {answer.strip()}\n")

if __name__ == "__main__":
    cleaned_data_file = 'cleaned_data.txt'
    output_file = 'general_info.txt'
    save_to_file(cleaned_data_file, output_file)
