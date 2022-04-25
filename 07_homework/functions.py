import json


def load_students():
    """ loads students infos from students.json file """
    file = open("students.json")
    students = json.load(file)
    file.close()
    return students


def load_professions():
    """ loads data about professions from professions.json file """
    file = open("professions.json")
    professions = json.load(file)
    file.close()
    return professions

# def load_students():
#     """ loads students infos from students.json file """
#     with open("students.json", "r", encoding="utf-8") as file:
#         return json.load(file)
#
#
# def load_professions():
#     """ loads data about professions from professions.json file """
#     with open("professions.json", "r", encoding="utf-8") as file:
#         return json.load(file)


def get_student_by_pk(pk):
    """ gets student info by 'pk' key """
    students = load_students()
    for student in students:
        if pk == str(student['pk']):
            return student


def get_profession_by_title(profession_title):
    """ gets profession info by 'title' key """
    professions = load_professions()
    for profession in professions:
        if profession_title == profession['title']:
            return profession


# def check_fitness(student, profession):
#     student, skills = get_student_by_pk(student)
#     has_set = set(skills)
#     requested_skills = set(get_profession_by_title(profession))
#     has_value = has_set & requested_skills
#     lacks_value = requested_skills - has_value
#     fit_percent_value = (len(has_value) * 100) / len(requested_skills)
#     result_dict = {
#         "has": has_value,
#         "lacks": lacks_value,
#         "fit_percent": fit_percent_value
#     }
#     return result_dict


def check_fitness(student_number, profession_title):
    """ checks if student fits for particular job """
    student = get_student_by_pk(student_number)
    student_skills = set(student['skills'])
    student_learns = set(student['learns'])

    profession = get_profession_by_title(profession_title)
    profession_skills = set(profession['skills'])

    # check what skills for profession the student doesn't have
    lacks_skills = profession_skills.difference(student_skills)

    # check what student skills are in the set of needed skills for the profession
    relevant_skills = student_skills.intersection(profession_skills)

    fit_percent = int(len(relevant_skills) / len(profession_skills) * 100)

    fitness_info = {
                    "full_name": student['full_name'],
                    "has": list(student_skills),
                    "relevant": list(relevant_skills),
                    "lacks": list(lacks_skills),
                    "learns": list(student_learns),
                    "fit_percent": fit_percent,
                    }
    return fitness_info
