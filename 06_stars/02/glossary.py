import csv

lib = {}

with open('glossary.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    for row in reader:
        lib[row[0].lower()] = row[1]

while True:
    user_term = input('Введите термин\n').lower().strip()
    if user_term in lib.keys():
        print(f'{user_term.capitalize()} - {lib[user_term]}')
    elif user_term == 'выйти':
        break
    else:
        print(f'По вашему запросу ничего не найдено, могу предложить:')
        for key in lib.keys():
            print(f'- {key}')

print('Закончили!')