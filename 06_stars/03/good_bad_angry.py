import csv


with open('list.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        if int(row[1]) >= 75:
            with open('passed.txt', 'a', encoding='utf-8') as f:
                f.write(row[0] + '\n')
        else:
            with open('failed.txt', 'a', encoding='utf-8') as f:
                f.write(row[0] + '\n')
