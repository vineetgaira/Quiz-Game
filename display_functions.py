import colorama
from colorama import Fore
colorama.init(autoreset=True)

def multiple_categories():
    print(Fore.BLUE+"Catagories.....\n"
          "1 : General Knowledge\n" \
          "2 : Entertainment : Books\n" \
          "3 : Entertainment : Film\n" \
          "4 : Entertainment : Music\n" \
          "5 : Entertainment : Musicals and Theaters\n" \
          "6 : Entertainment : Television\n" \
          "7 : Entertainment : Video Games\n" \
          "8 : Entertainment : Board Games\n" \
          "9 : Science and Nature \n" \
          "10 : Science : Computers\n" \
          "11 : Science : Mathematics\n" \
          "12 : Mythology\n" \
          "13 : Sports\n" \
          "14 : Geography\n" \
          "15 : History\n" \
          "16 : Politics\n" \
          "17 : Art\n" \
          "18 : Celebrities\n" \
          "19 : Animals\n" \
          "20 : Vehicles\n" \
          "21 : Entertainment : Comics\n" \
          "22 : Science : Gadgets\n" \
          "23 : Entertainment : Japanese Anime & Manga\n" \
          "24 : Entertainment : Cartoon and Animations" \
            )

def difficulty_level():
    print(Fore.BLUE+"\nDifficulty levels...\n"
          "1 : Easy\n"
          "2 : Medium\n"
          "3 : Hard")
    
def type_questions():
    print(Fore.BLUE+"\nType of question...\n" \
          "1 : Multiple Choice\n" \
          "2 : True or False")