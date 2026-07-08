import requests
import random
import html
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from constants import CATEGORIES, TYPE, DIFFICULTY_LEVELS
from display_functions import multiple_categories, difficulty_level, type_questions



def get_category():
    while True:
        try:
            get_category=int(input(Fore.BLUE+"Please select a category :"))
            if get_category in range(1,25):
                return get_category
            else:
                print(Fore.RED+"Please select a valid option..")
        except ValueError:
            print(Fore.RED+"Pleae enter a valid option between 1-24.")

def get_type():
    valid_choices={1,2}
    while True:
        try:
            get_type=int(input(Fore.BLUE+"Please select a type :"))
            if get_type in valid_choices:
                return get_type
            else:
                print(Fore.RED+"Please enter a valid option.")
        except ValueError:
            print(Fore.RED+"Pleae enter a number between 1-3.")

def get_difficulty_level():
    valid_choices={1,2,3}
    while True:
        try:
            get_level=int(input(Fore.BLUE+"Please select a difficulty level:"))
            if get_level in valid_choices:
                return get_level
            else:
                print(Fore.RED+"Please enter a valid option.")
        except ValueError:
            print(Fore.RED+"Pleae enter a number between 1-3.")
    

def get_questions_amount():
    print(Fore.BLUE+"You can select a amount of questions between 5-50.")
    while True:
        try:
            give_amount=int(input(Fore.BLUE+"Please enter a amount of questions between 5-50:"))
            if give_amount in range(5,51):
                return give_amount
            else:
                print(Fore.RED+"Please enter a number between 5-50.")
        except ValueError:
            print(Fore.RED+"Pleae enter a number between 5-50.")

def url_modifier(amount,category,level,type):
    
    url = f"https://opentdb.com/api.php?amount={amount}&category={CATEGORIES[category]}&difficulty={DIFFICULTY_LEVELS[level]}&type={TYPE[type]}"

    return url 


def display_questions(url):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED+f"Error: {e}")

    questions = data["results"]
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

def play_quiz():
    while True:
        multiple_categories()
        category=get_category()
        type_questions()
        type=get_type()
        difficulty_level()
        level=get_difficulty_level()
        amount=get_questions_amount()
        url=url_modifier(amount,category,level,type)
        score=display_questions(url)
        print(Fore.LIGHTGREEN_EX+f"Your score is {score}/{amount}")
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