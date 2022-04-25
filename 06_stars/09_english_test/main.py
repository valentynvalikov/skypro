import csv

filename = "english_test.csv"

questions = {}

with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    i = 1
    for row in reader:
        questions[i] = {'question': row['question'], 'answer 1': row['answer 1'], 'answer 2': row['answer 2'], 'correct answer': row['correct answer']}
        i += 1

for i, question in questions.items():
    print(f"Question {i}. {question['question']}")
    answer = input(f"[1] {question['answer 1']}\n"
                   f"[2] {question['answer 2']}\n")
    if question['answer ' + answer] == question['correct answer']:
        print("Верно")
    else:
        print(f"Нет. Верный ответ – {question['correct answer']}")
