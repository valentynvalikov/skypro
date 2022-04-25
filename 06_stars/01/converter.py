with open('miles.txt', 'r', encoding='utf-8') as file:
    kms = []
    for value in file:
        kms.append(float(value) * 1.609)

with open('kms.txt', 'a', encoding='utf-8') as file:
    for value in kms:
        file.write(str(round(value, 2)) + '\n')
