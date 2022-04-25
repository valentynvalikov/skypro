employees = [

    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семеновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнев Константин Игоревич", "vaccinated": False},
]
vaccinated = []
not_vaccinated = []
for vac in employees:
    if vac["vaccinated"]:
        vaccinated.append(vac["fio"])
    else:
        not_vaccinated.append(vac["fio"])


print("Вакцинированные:", '\n'.join(vaccinated), "Остальные:", '\n'.join(not_vaccinated), sep='\n')


# fish = [
#
#     {"specie": "Белуга", "water": "fresh"},
#     {"specie": "Карась", "water": "fresh"},
#     {"specie": "Красноперка", "water": "fresh"},
#
#     {"specie": "Морской окунь", "water": "sea"},
#     {"specie": "Тунец", "water": "sea"},
#     {"specie": "Скумбрия", "water": "sea"},
#
# ]
#
# user_fish = input("Рыба моей мечты\n")
#
#
# def get_fish(user_fish):
#     for i in fish:
#         if i['specie'] == user_fish.capitalize():
#             return i['specie'], i['water']
#
#
# get_fish(user_fish)