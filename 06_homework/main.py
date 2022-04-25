import random

while True:
    user_name = input('Введите ваше имя.\n').strip()
    if '  ' in user_name:
        print('В имени может быть не более одного пробела подряд')
    else:
        break


words_file = 'words.txt'
stats_file = 'history.txt'


def get_words(filename):
    """ function to get homework """
    words_list = []
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line.replace('\n', '')
            words_list.append(line.replace('\n', ''))
    return words_list


def save_stats(user, score, filename):
    """ function to save game statistics """
    with open(filename, 'a', encoding="utf-8") as file:
        if file.write(user + '  ' + str(score) + '\n'):
            return True


def show_stats(filename):
    """ function to read and show game statistics """
    with open(filename, 'r', encoding="utf-8") as file:
        total_games = 0
        scores = []
        for line in file:
            total_games += 1
            name, score = line.split('  ')
            scores.append(int(score))
        print(f'\nВсего игр сыграно: {total_games}')
        print(f'Максимальный рекорд: {max(scores)}')


""" main game cycle """
user_score = 0
words = get_words(words_file)
for word in words:
    shuffled_word = random.sample(word, len(word))
    user_answer = input(f'\nУгадайте слово: {"".join(shuffled_word)}\n').lower().strip()
    if user_answer == word:
        print('Верно! Вы получаете 10 очков.')
        user_score += 10
    else:
        print(f'Неверно! Верный ответ – {word}')


save_stats(user_name, user_score, stats_file)

show_stats(stats_file)
