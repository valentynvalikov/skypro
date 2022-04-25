class Teller:
    def __init__(self):
        self._shots = 1

    def ask(self, topic):
        if self._shots == 1:
            if topic == "дорога":
                self._shots = 0
                return "Отправляйся на север, держись самого края леса," \
                       "найдешь пещеру, пройдешь внутри, от нее 2-3 лиги до городка"
            elif topic == "виверна":
                self._shots = 0
                return "Победить виверну можно только магическим оружием." \
                       "Спроси в городке сотрудников гильдии магического метода"
            elif topic == "дракон":
                self._shots = 0
                return "За сломанной горой в скалах живет дракон." \
                       "С ним вообще никогда проблем не было"
        return "Ты исчерпал свои попытки, странник. Уходи!"


teller = Teller()
print(teller.ask("дракон"))
print(teller.ask("виверна"))
print(teller.ask("дракон"))