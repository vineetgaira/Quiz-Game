import requests
import random
from pprint import pprint

URL = "https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=multiple"

RESPONSE = requests.get(URL)
DATA = RESPONSE.json()

QUESTION = DATA["results"]




def display_quesions():

    for  question in QUESTION:
        options = question["incorrect_answers"] + [question["correct_answer"]]

        random.shuffle(options)

        print(question["question"])

        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
        check_answer(options,question)
        

def get_user_answer():
    valid_choices={1,2,3,4}
    while True:
        try:
            choice = int(input("Choice: "))
            if choice in valid_choices:
                return choice
            else:
                print("Please enter a valid choice.")
                continue
        except ValueError:
            print("Please enter a valid integer choice.")
            continue
 
def check_answer(options,question):
    choice=get_user_answer()
    score=0
    if options[choice - 1] == question["correct_answer"]:
        print("Correct!")
        score+=1
        return score
    else:
        print("Wrong!")
   
                    
def calculate_score():
    score=check_answer()
    
    print("Your total score :\n" \
    f"Score : {score}/10")

def display_result():
    pass
def play_quiz():
    display_quesions()
    get_user_answer()
    calculate_score()
if __name__=="__main__":
    play_quiz()