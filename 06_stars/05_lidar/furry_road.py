def make_word_ending(number, word_end1='', word_end2='', word_end3='') -> str:
    """
    makes ending of the word according to specified number
    :param number:
    :param word_end1: ''
    :param word_end2: 'а'
    :param word_end3: 'о'
    :return:
    """
    number = str(number)
    if number[-2:] in ["11", "12", "13", "14", "15", "16", "17", "18", "19"]:
        return word_end1
    elif number[-1] in ["0", "5", "6", "7", "8", "9"]:
        return word_end1
    elif number[-1] == "1":
        return word_end2
    elif number[-1] in ["2", "3", "4"]:
        return word_end3


with open('furry_road3.txt', 'r', encoding='utf-8') as file:
    content = file.readlines()
    lines = []
    for line in content:
        line = line.strip().split()
        lines.append(line)

c = [0, 2]

for i in lines:
    if i[c[1]] == "False":
        print(f"{c[0] * 3} метр{make_word_ending(c[0] * 3, 'ов', '', 'а')} проехали - едем вперёд")
    elif i[c[1]] == "True" and i[c[1] - 1] == "False":
        print(f"{c[0] * 3} метр{make_word_ending(c[0] * 3, 'ов', '', 'а')} проехали - возьми вправо")
        c[1] -= 1
    elif i[c[1]] == "True" and i[c[1] - 1] == "True" and i[c[1] + 1] == "False":
        print(f"{c[0] * 3} метр{make_word_ending(c[0] * 3, 'ов', '', 'а')} проехали - возьми влево")
        c[1] += 1
    c[0] += 1

