find = input("Введите искомый текст\n")


with open('messages.txt', 'r', encoding='utf-8') as file:
    i = 0
    for line in file:
        if find.lower() in line.lower():
            i += 1
    print(f"Ищем: {find}")
    print(f"Найдено сообщений: {i}")
