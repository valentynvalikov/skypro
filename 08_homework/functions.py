import json
import random


def load_json(filename) -> json:
    """Load json from file with path 'filename'"""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)


def shuffle_questions(questions_list, number_of_questions) -> list:
    """Shuffles a list using 'random.sample'
    Takes list of questions as 'questions_list' argument
    Returns specified in 'number_of_questions' argument number of shuffled questions as a list
    """
    return random.sample(questions_list, number_of_questions)


def stats(score) -> str:
    """Counts statistics from list with values that looks like [20, 30, False, 10, False]
    And returns statistics as a string
    """
    total_correct_answers = len(score) - score.count(False)
    return (f"That's all!\n"
            f"{total_correct_answers} correct answers out of {len(score)}\n"
            f"Total score: {sum(score)}\n")
