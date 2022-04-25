import csv

with open('expenses.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    total_items = 0
    total_sum = 0
    for row in reader:
        total_items += 1
        total_sum += int(row[1])

print(f"Всего позиций: {total_items}\n"
      f"Сумма: {total_sum}")
