import requests
import random
import html
import colorama
from colorama import Fore
colorama.init(autoreset=True)
from constants import CATEGORIES, TYPE, DIFFICULTY_LEVELS
from display_functions import multiple_categories, difficulty_level, type_questions
from input_functions import get_category,get_difficulty_level,get_questions_amount,get_type



def create_url(amount,category,level,question_type):
    
    url = f"https://opentdb.com/api.php?amount={amount}&category={CATEGORIES[category]}&difficulty={DIFFICULTY_LEVELS[level]}&type={TYPE[question_type]}"

    return url 


def display_questions(url):

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        print(Fore.RED+f"Error: {e}")
        return 0

    questions = data["results"]
    
    if not questions:
        print(Fore.RED+"No questions were found please try a different setting.")
        return 0
    
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
            print("-"*40)
        else:
            print(Fore.RED+f"Wrong! the correct answer was {Fore.LIGHTGREEN_EX+html.unescape(question['correct_answer'])}")
    return score
        
def get_user_answer(options, correct_answer):
    valid_choices={1,2,3,4}
    while True:
        try:
            choice=int(input(Fore.LIGHTBLUE_EX+"\nEnter your choice:"))
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
        question_type=get_type()
        difficulty_level()
        level=get_difficulty_level()
        amount=get_questions_amount()
        url=create_url(amount,category,level,question_type)
        score=display_questions(url)
        percentage=score/amount*100
        if percentage>=90:
            print(Fore.LIGHTGREEN_EX+"Excellent!")
        elif percentage>=70 and percentage<90:
            print(Fore.LIGHTGREEN_EX+"Great!")
        elif percentage>=50 and percentage<70:
            print(Fore.LIGHTGREEN_EX+"Good!")
        elif percentage<=50:
            print(Fore.LIGHTGREEN_EX+"Keep practicing!")

        print(Fore.LIGHTGREEN_EX+f"Score : {score}/{amount}")
        print(Fore.LIGHTGREEN_EX+f"Percentage : {percentage:.2f}%")
        
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