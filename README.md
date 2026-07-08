<div align="center">

# 🧠 Quiz Game CLI

### *How much do you really know? Find out — one question at a time.*

```
   ┌───────────────────────────────┐
   │  Q: What is the capital of    │
   │     France?                   │
   │                                │
   │  1. Berlin      2. Madrid      │
   │  3. Paris ✅    4. Rome        │
   └───────────────────────────────┘
        🎯  24 Categories · 3 Difficulties · Multiple Choice & True/False
```

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-API-000000?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenTDB](https://img.shields.io/badge/Powered%20By-OpenTDB-6E44FF?style=for-the-badge)
![Colorama](https://img.shields.io/badge/Colorama-Enabled-FFD43B?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Practice%20Project-orange?style=for-the-badge)

</div>

---

## ✨ Overview

**Quiz Game CLI** is an interactive, terminal-based trivia game that pulls live questions from the [Open Trivia Database](https://opentdb.com/) API. Choose your category, difficulty, question type, and round length — then test your knowledge with instant, color-coded feedback after every answer.

## 🎨 Preview

```
Catagories.....
1 : General Knowledge
2 : Entertainment : Books
...
24 : Entertainment : Cartoon and Animations
Please select a category :9

Type of question...
1 : Multiple Choice
2 : True or False
Please select a type :1

Difficulty levels...
1 : Easy
2 : Medium
3 : Hard
Please select a difficulty level:2

You can select a amount of questions between 5-50.
Please enter a amount of questions between 5-50:5

Question 1/5
What is the chemical symbol for gold?
1. Ag
2. Au
3. Gd
4. Pb

Enter your choice:2
Correct!
----------------------------------------
...
Great!
Score : 4/5
Percentage : 80.00%
Do you wanna play another round(y/n):
```

## 🧩 Features

<div align="center">

| Feature | Description |
|:---|:---|
| 🌐 | **Live Questions** — fetched fresh from the OpenTDB API every round |
| 🗂️ | **24 Categories** — from General Knowledge to Anime & Manga |
| 🎚️ | **3 Difficulty Levels** — Easy, Medium, Hard |
| ❓ | **2 Question Types** — Multiple Choice or True/False |
| 🔢 | **Custom Round Length** — choose 5 to 50 questions per game |
| 🔀 | **Shuffled Answers** — options are randomized every question |
| 🎨 | **Colorized Output** — clear, color-coded prompts and results via `colorama` |
| 🏆 | **Score Summary** — final score, percentage, and a performance verdict |
| 🔁 | **Replay Loop** — jump straight into another round |

</div>

## 🗂️ Trivia Categories

<details>
<summary>Click to expand all 24 categories</summary>

| # | Category | # | Category |
|:-:|:---|:-:|:---|
| 1 | General Knowledge | 13 | Sports |
| 2 | Entertainment: Books | 14 | Geography |
| 3 | Entertainment: Film | 15 | History |
| 4 | Entertainment: Music | 16 | Politics |
| 5 | Entertainment: Musicals & Theaters | 17 | Art |
| 6 | Entertainment: Television | 18 | Celebrities |
| 7 | Entertainment: Video Games | 19 | Animals |
| 8 | Entertainment: Board Games | 20 | Vehicles |
| 9 | Science & Nature | 21 | Entertainment: Comics |
| 10 | Science: Computers | 22 | Science: Gadgets |
| 11 | Science: Mathematics | 23 | Entertainment: Japanese Anime & Manga |
| 12 | Mythology | 24 | Entertainment: Cartoon and Animations |

</details>

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- An active internet connection (questions are fetched live from OpenTDB)

### Installation

```bash
git clone https://github.com/vineetgaira/Quiz-Game.git
cd Quiz-Game
pip install -r requirements.txt
```

### Run it

```bash
python main.py
```

## 🕹️ How to Play

1. **Pick a category** from the list of 24 trivia topics.
2. **Choose a question type** — Multiple Choice or True/False.
3. **Select a difficulty** — Easy, Medium, or Hard.
4. **Set the round length** — anywhere from 5 to 50 questions.
5. Answer each question by entering the number of your choice.
6. Get instant feedback — ✅ correct or ❌ the right answer revealed.
7. See your final **score**, **percentage**, and a performance verdict.
8. Choose `y` to play another round, or `n` to exit.

## 🗂️ Project Structure

```
Quiz-Game/
├── main.py                # Entry point — game loop, scoring & API requests
├── constants.py            # Category IDs, difficulty levels & question limits
├── display_functions.py     # Prints category, type & difficulty menus
├── input_functions.py        # Validates and returns user menu selections
├── requirements.txt            # Project dependencies
├── src/                          # Reserved for future modularization
├── tests/                         # Reserved for future test coverage
└── docs/                           # Reserved for future documentation
```

## 🧠 How It Works

1. User selections (category, type, difficulty, amount) are mapped to OpenTDB's expected values via lookup dictionaries in `constants.py`.
2. A request URL is built and sent to the OpenTDB API using `requests`.
3. Each returned question's answers are combined and **shuffled** so the correct answer isn't always in the same position.
4. HTML entities in questions/answers (e.g. `&quot;`) are decoded with `html.unescape()` for clean display.
5. The user's choice is checked against the correct answer, the score is tallied, and a final percentage-based verdict is shown at the end of the round.

## 🛠️ Built With

- 🐍 **Python** — core game logic
- 🌐 **Requests** — fetching live trivia data from the OpenTDB API
- 🎨 **Colorama** — cross-platform colored terminal text
- 🧾 **html (stdlib)** — decoding HTML-escaped question text

## 📈 Roadmap

- [ ] Move logic into `src/` for cleaner structure
- [ ] Add unit tests under `tests/`
- [ ] Add a timer per question for extra challenge
- [ ] Track high scores across sessions
- [ ] Add a "random category" quick-play mode

## ⚠️ Disclaimer

This is a **practice project** built for learning Python fundamentals — API integration, input validation, and building an engaging CLI experience. Trivia content is sourced entirely from the [Open Trivia Database](https://opentdb.com/) and is not owned by this project.

## 📄 License

Open source — free to use, learn from, and build upon.

---

<div align="center">

Made with 🐍 Python — *Damn I loved making this.* 🧠

</div>
