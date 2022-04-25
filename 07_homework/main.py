import functions as f


def main():
    print("Здравствуйте. Здесь Вы можете проверить подходит ли студент для работы по конкретной профессии")

    while True:
        student_number = input("Введите номер студента\n")
        student_number = student_number.strip()

        if f.get_student_by_pk(student_number):
            student_info = f.get_student_by_pk(student_number)
            break
        else:
            print("У нас нет такого студента\n")

    print(f"\nСтудент {student_info['full_name']}\n"
          f"Знает: {', '.join(student_info['skills'])}\n"
          f"Изучает: {', '.join(student_info['learns'])}\n")

    while True:
        profession_title = input(f"Выберите специальность для оценки студента {student_info['full_name']}\n")
        profession_title = profession_title.strip().capitalize()

        if f.get_profession_by_title(profession_title):
            fitness_dict = f.check_fitness(student_number, profession_title)
            break
        else:
            print("У нас нет такой специальности\n")

    fitness = f"\nПригодность {fitness_dict['fit_percent']}%\n"
    if len(fitness_dict['relevant']) != 0:
        fitness += f"{student_info['full_name']} знает: {', '.join(fitness_dict['relevant'])}\n"
    if len(fitness_dict['lacks']) != 0:
        fitness += f"{student_info['full_name']} не знает: {', '.join(fitness_dict['lacks'])}\n"

    print(fitness)

    repeat = input("Хотите проверить ещё одного студента?\n"
                   "Если да  - нажмите Enter\n"
                   "Если нет - введите любой символ и нажмите Enter\n")
    if repeat == '':
        main()
    else:
        quit("До свидания")


if __name__ == '__main__':
    main()



