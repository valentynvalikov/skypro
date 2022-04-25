import csv

filename = "snakes_scores.csv"

scores = {}

with open(filename, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    i = 1
    for row in reader:
        scores[row['Имя змеи']] = {'Техника': row['Техника'], 'Внешний вид': row['Внешний вид'], 'Шипение': row['Шипение']}
        i += 1

for name, marks in scores.items():
    total = 0
    for i in list(marks.values()):
        total += int(i)
    avg = round(total / len(marks.values()), 2)
    print(f"{name}: {avg}")

