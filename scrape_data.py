import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    questions = []
    answers = []
    
    for item in soup.find_all('div', class_='col-lg-6'):
        question = item.find('h3').get_text().strip()
        answer = item.find('p').get_text().strip()
        questions.append(question)
        answers.append(answer)
    
    return questions, answers

if __name__ == "__main__":
    url = 'https://trivia.fyi/random'
    questions, answers = scrape_website(url)
    
    # Save the raw data to a file for further processing
    with open('raw_data.txt', 'w') as file:
        for question, answer in zip(questions, answers):
            file.write(f"{question}+++{answer}\n")
