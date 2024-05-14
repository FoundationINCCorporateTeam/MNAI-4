def load_data(filename):
    data = {}
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(" +++$+++ ")
            if len(parts) == 4:
                _, _, question, answer = parts
                data[question.lower()] = answer
    return data

def get_answer(data, query):
    query = query.lower()
    return data.get(query, "I'm sorry, I don't have an answer for that question.")

if __name__ == "__main__":
    data_file = 'general_info.txt'
    data = load_data(data_file)
    
    print("Welcome to the trivia chatbot! Ask me anything or type 'exit' to quit.")
    while True:
        user_input = str(input("You: "))
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        answer = get_answer(data, user_input)
        print(f"Bot: {answer}")
