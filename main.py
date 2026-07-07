import requests
import random
import html
import colorama
from colorama import Fore
colorama.init(autoreset=True)


URL = "https://opentdb.com/api.php?amount=11&category=9&difficulty=hard&type=multiple"


RESPONSE = requests.get(URL)
DATA = RESPONSE.json()

QUESTION = DATA["results"]

def display_questions(questions):
    score=0
    for number,question in enumerate(questions,start=1):
        print(Fore.LIGHTBLUE_EX+f"\nQuestion {number}/{len(questions)}")
    

        options = question['incorrect_answers'] +  [question['correct_answer']]
        random.shuffle(options)
    
        print(Fore.LIGHTCYAN_EX+html.unescape(question['question']))

        for i, option in enumerate(options, start=1):
            print(Fore.LIGHTCYAN_EX+f"{i}. {html.unescape(option)}")    

        if get_user_answer(options,question['correct_answer']):
            score+=1 
            print(Fore.LIGHTGREEN_EX+"Correct!")
        else:
            print(Fore.RED+f"Wrong! the correct answer was {Fore.LIGHTGREEN_EX+html.unescape(question['correct_answer'])}")
    return score
        
def get_user_answer(options, correct_answer):
    valid_choices={1,2,3,4}
    while True:
        try:
            choice=int(input(Fore.LIGHTBLUE_EX+"Enter your choice:"))
            if choice in valid_choices:
                if options[choice-1]==correct_answer:
                    return True
                else:
                    return False
            else:
                print(Fore.RED+"Please select a valid option.")
        except ValueError:
            print(Fore.RED+"Please select a valid option.")

def check_answer():
    pass
    
 
def calculate_score():
    pass


def display_result():
    pass

def play_quiz():
    while True:
        score=display_questions(QUESTION)
        print(Fore.LIGHTGREEN_EX+f"Your score is {score}/11")
        while True:
            user_exit=input(Fore.LIGHTBLUE_EX+"Do you wanna play another round(y/n):").lower()
            if user_exit=="y":
                break
            elif user_exit=="n":
                print(Fore.LIGHTCYAN_EX+"Thanks for quizzing....")
                return
            else:
                print(Fore.RED+"Please enter a y/n.")
                continue
    
if __name__=="__main__":
    play_quiz()