import requests
import json
import random
import classes.basic_word as bw


def word_ending(number, word_end1, word_end2, word_end3) -> str:
    """
    makes ending of the word according to specified number
    :param number:
    :param word_end1: ''
    :param word_end2: 'а'
    :param word_end3: 'о'
    :return:
    """
    if number[-2:] in ["11", "12", "13", "14", "15", "16", "17", "18", "19"]:
        return word_end1
    elif number[-1] in ["0", "5", "6", "7", "8", "9"]:
        return word_end1
    elif number[-1] == "1":
        return word_end2
    elif number[-1] in ["2", "3", "4"]:
        return word_end3


def get_json_from_server(url) -> json:
    """
    gets json from server
    :param url:
    :return: json
    """
    response = requests.get(url)
    return response.json()


def load_random_word(url):
    """
    gets json from server and returns an instance of word for the game
    :param url:
    :return: object
    """
    words_json = get_json_from_server(url)
    random_word = random.choice(words_json)

    base_word = random_word['word']
    subwords = random_word['subwords']

    return bw.BasicWord(base_word, subwords)
