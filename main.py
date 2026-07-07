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

        for number,question in enumerate(questions,start=1):
            print(f"\nQuestion {number}/{len(questions)}")
            print(html.unescape(question['question']))

        for i, option in enumerate(options, start=1):
            print(f"{i}. {html.unescape(option)}")    

        if get_user_answer(options,question['correct_answer']):
            score+=1 
            print("Correct!")
        else:
            print(f"Wrong! the correct answer was {question['correct_answer']}")
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
    while True:
        score=display_questions(QUESTION)
        print(f"Your score is {score}/10")
        while True:
            user_exit=input("Do you wanna play another round(y/n):").lower()
            if user_exit=="y":
                break
            elif user_exit=="n":
                print("Thanks for quizzing....")
                return
            else:
                print("Please enter a y/n.")
                continue

        


if __name__=="__main__":
    play_quiz()