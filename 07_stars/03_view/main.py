users = [{
    "pk": 1,
    "fio": {
       "f": "Валиков",
       "i": "Вал",
       "o": "Сергеевич"
    }
},
    {
    "pk": 2,
    "fio": {
        "f": "Альшевский",
        "i": "Марк",
        "o": "Игоревич"
    }
},
    {
    "pk": 3,
    "fio": {
       "f": "Бесов",
       "i": "Хрен",
       "o": "Моржович"
    }
}]
data_map = {"f": "фамилия", "i": "имя", "o": "отчество"}


def mapper(data, data_map) -> dict:
    mapped_data = []
    for user in data:
        mapped_user = {}
        for key in user['fio'].keys():
            mapped_user[data_map[key]] = user['fio'][key]
        mapped_data.append(mapped_user)
    return mapped_data


print(mapper(users, data_map))