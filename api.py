url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=multiple"

response=requests.get(url)
data=response.json()

question = data["results"][0]

options = question["incorrect_answers"] + [question["correct_answer"]]

random.shuffle(options)

print(question["question"])

for i, option in enumerate(options, start=1):
    print(f"{i}. {option}")

choice = int(input("Choice: "))

if options[choice - 1] == question["correct_answer"]:
    print("Correct!")
else:
    print("Wrong!")
