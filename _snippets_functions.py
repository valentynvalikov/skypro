def make_word_ending(number, word_end1='', word_end2='', word_end3='') -> str:
    """
    добаляет окончание слова в соответствии с числом
    :param number:
    :param word_end1: ''
    :param word_end2: 'а'
    :param word_end3: 'о'
    :return: str
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


def get_json_from_server(url) -> json:
    """
    gets json from server
    :param url:
    :return: json
    """
    response = requests.get(url)
    return response.json()