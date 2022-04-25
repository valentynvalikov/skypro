import re

text = input("Введите название текста\n").lower().strip()
filename = 'texts/' + text + '.txt'

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
    matches = re.findall('[.!?][ \t\n\r]+[\"\'A-ZА-Я]', text)
    print(f"Предложений - {len(matches) + 1}")

with open(filename, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print(f"Строк - {len(lines)}")

with open(filename, 'r', encoding='utf-8') as file:
    text = file.read()
    matches = re.findall('[ \n]', text)
    print(f"Слов - {len(matches) + 1}")

with open(filename, 'r', encoding='utf-8') as file:
    symbols = file.read()
    print(f"Символов - {len(symbols)}")
