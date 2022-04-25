class Player:

    def __init__(self, name):
        self._name = name
        self._correct_words = []

    def get_user_name(self) -> str:
        """
        returns user name
        :return: str
        """
        return self._name

    def get_correct_words(self) -> set:
        """
        returns set of correct user's subwords
        :return: set
        """
        return set(self._correct_words)

    def set_correct_words(self, user_word):
        """
        appends user suggested word to set of used words
        :param user_word:
        """
        self._correct_words.append(user_word)

    def is_word_in_correct(self, user_word) -> bool:
        """
        returns True if user-suggested word is in the set 'used_words'
        otherwise returns False
        :param user_word:
        :return: bool
        """
        if user_word in set(self._correct_words):
            return True
        return False
