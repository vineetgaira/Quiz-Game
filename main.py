import requests
import random
from pprint import pprint
import html


URL = f"https://opentdb.com/api.php?amount=11&category=9&difficulty=easy&type=multiple"


RESPONSE = requests.get(URL)
DATA = RESPONSE.json()

QUESTION = DATA["results"]

def display_questions(questions):
    score=0
    for question in questions:
        options = question['incorrect_answers'] +  [question['correct_answer']]
        random.shuffle(options)

        print(html.unescape(question['question']))

        for i, option in enumerate(options, start=1):
            print(f"{i}. {html.unescape(option)}")    

        if get_user_answer(options,question['correct_answer']):
            score+=1 
    return score


        
def get_user_answer(options, correct_answer):
    valid_choices={1,2,3,4}
    while True:
        try:
            choice=int(input("Enter your choice:"))
            if choice in valid_choices:
                if options[choice-1]==correct_answer:
                    return True
                else:
                    return False
            else:
                print("Please select a valid option.")
        except ValueError:
            print("Please select a valid option.")
        
    

def check_answer():
    pass
    
 
def calculate_score():
    pass


def display_result():
    pass

def play_quiz():
    display_quesions(QUESTION)
    


if __name__=="__main__":
    play_quiz()