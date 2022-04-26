class Question:
    """Class that deals with asking questions and performs main logic"""

    _user_answer = None

    def __init__(self, question, difficulty, correct_answer):
        self._question = question
        self._difficulty = int(difficulty)
        self._correct_answer = correct_answer
        self._mark = self._difficulty * 10

    def user_answer(self, user_answer=None) -> str:
        """Setter/getter for user answer to/from '_user_answer' var"""
        if user_answer:
            self._user_answer = user_answer
        return self._user_answer

    def get_points(self) -> int:
        """Returns mark for current question as 'int'.
        Mark depends on difficulty: for 1 user gets 10 points, for 5 user gets 50 points.
        """
        if self.is_correct():
            return self._mark
        else:
            return False

    def is_correct(self) -> bool:
        """Returns True, if user's answer matches correct answer, otherwise returns False"""
        if self._correct_answer.lower() == self._user_answer.lower():
            return True
        else:
            return False

    def build_question(self) -> str:
        """Returns question in understandable for user manner, for example:
        Question: What do people often call American flag?
        Difficulty 4/5
        """
        return f"Question: {self._question}\n"\
               f"Difficulty {self._difficulty}/5"

    def build_feedback(self) -> str:
        """Returns feedback to user depending on correctness of user's answer"""
        if self.is_correct():
            return f"Correct answer, you've got {self._mark} points\n"
        else:
            return f"Incorrect answer, correct answer is {self._correct_answer}\n"
