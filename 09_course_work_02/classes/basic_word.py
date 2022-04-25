class BasicWord:

    def __init__(self, base_word, subwords):
        self._base_word = base_word
        self._subwords = subwords
        self._number_of_subwords = len(self._subwords)

    def get_word(self) -> str:
        """
        returns basу word fo game
        :return: str
        """
        return self._base_word

    def get_number_of_subwords(self) -> int:
        """
        returns number of possible subwords
        :return: int
        """
        return self._number_of_subwords

    def is_in_subwords(self, user_word) -> bool:
        """
        checks if word inputted by user is in the list of subwords
        :param user_word:
        :return: bool
        """
        if user_word in self._subwords:
            return True
        else:
            return False
