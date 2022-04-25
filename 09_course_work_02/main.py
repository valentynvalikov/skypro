import functions as f
import classes.player as p


def main():

    json_url = 'https://jsonkeeper.com/b/5WCV'

    user_name = input("Введите имя игрока\n").strip()

    player = p.Player(user_name)

    print(f"Привет, {player.get_user_name()}!")

    bw = f.load_random_word(json_url)
    number_of_subwords = bw.get_number_of_subwords()
    base_word = bw.get_word().upper()

    print(f"Составьте {number_of_subwords} слов{f.word_ending(str(number_of_subwords), '', 'о', 'а')} из слова {base_word}\n"
          "Слова должны быть не короче 3 букв\n"
          "Чтобы закончить игру, угадайте все слова или напишите 'стоп'\n"
          "Поехали, ваше первое слово?")

    words_left_count = number_of_subwords

    while len(player.get_correct_words()) < number_of_subwords:

        suggested_word = input().strip().lower()

        if suggested_word == "стоп":
            print(f"Игра завершена!\n"
                  f"Вы угадали {len(player.get_correct_words())} слов{f.word_ending(str(words_left_count), '', 'о', 'а')}")
            quit()
        elif player.is_word_in_correct(suggested_word) and bw.is_in_subwords(suggested_word):
            player.set_correct_words(suggested_word)
            print(f"Верно, но вы уже отгадали это слово\n"
                  f"Осталось угадать {words_left_count} слов{f.word_ending(str(words_left_count), '', 'о', 'а')}")
        elif bw.is_in_subwords(suggested_word):
            player.set_correct_words(suggested_word)
            words_left_count = number_of_subwords - len(player.get_correct_words())
            print(f"Верно\nОсталось угадать {words_left_count} слов{f.word_ending(str(words_left_count), '', 'о', 'а')}")
        else:
            print(f"Неверно\nОсталось угадать {words_left_count} слов{f.word_ending(str(words_left_count), '', 'о', 'а')}")

    print("Cлова закончились, игра завершена!\n"
          f"Вы угадали {len(player.get_correct_words())} слов{f.word_ending(str(words_left_count), '', 'о', 'а')}")


if __name__ == "__main__":
    main()
