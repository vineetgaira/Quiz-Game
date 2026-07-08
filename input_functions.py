import colorama
from colorama import Fore
colorama.init(autoreset=True)
from constants import MIN_QUESTIONS, MAX_QUESTIONS

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
    print(Fore.BLUE+"\nYou can select a amount of questions between 5-50.")
    while True:
        try:
            give_amount=int(input(Fore.BLUE+F"Please enter a amount of questions between {MIN_QUESTIONS}-{MAX_QUESTIONS-1}:"))
            if give_amount in range(MIN_QUESTIONS,MAX_QUESTIONS):
                return give_amount
            else:
                print(Fore.RED+F"Please enter a number between {MIN_QUESTIONS}-{MAX_QUESTIONS-1}")
        except ValueError:
            print(Fore.RED+f"Pleae enter a number between {MIN_QUESTIONS}-{MAX_QUESTIONS-1}.")