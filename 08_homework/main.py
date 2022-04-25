import classes.question as q
import functions as f

questions_file = 'questions.json'
number_of_questions = 5


def main():
    while True:
        score = []

        print("The Game has begun!\n")

        questions = f.load_json(questions_file)
        shuffled_questions = f.shuffle_questions(questions, number_of_questions)

        for item in shuffled_questions:
            question = q.Question(item['q'], int(item['d']), item['a'])

            print(question.build_question())
            user_answer = question.user_answer()
            while True:
                if user_answer is None or user_answer == "":
                    user_answer = input("Enter your answer\n").strip()
                else:
                    break
            question.user_answer(user_answer)
            print(question.build_feedback())

            score.append(question.get_points())

        print(f.stats(score))

        repeat = input("Play again?\n"
                       "Yes? - press Enter\n"
                       "No? - print any symbol and press Enter\n")
        if repeat == "":
            main()
        else:
            print("Good bye!")
            quit()


if __name__ == "__main__":
    main()
