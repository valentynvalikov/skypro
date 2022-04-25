class Hero:
    _levels = {2: 30, 3: 60, 4: 120, 5: 240, 6: 480}

    def __init__(self, name):
        self._name = name
        self._health = 100
        self._experience = 0
        self._level = 1

    def set_experience(self, experience):
        self._experience += experience
        self.set_level()
        self.set_health()
        return experience

    def set_level(self):
        for level, experience in self._levels.items():
            if self._experience <= experience:
                self._level = level
                break

    def set_health(self):
        for level in self._levels.keys():
            if self._level == level:
                if ((self._health * 1.5) % 10) > 0:
                    self._health = round(self._health * 1.5 - ((self._health * 1.5) % 10) + 10)
                    break
                else:
                    self._health = round(self._health * 1.5)
                    break

    def get_experience(self):
        return self._experience

    def get_level(self):
        return self._level

    def get_health(self):
        return self._health


z = Hero("Z")

print(f"Уровень - {z.get_level()} | Здоровье - {z.get_health()} | Опыт - {z.get_experience()}\n")

print(f"Добавлено {z.set_experience(16)} баллов опыта\n")

print(f"Уровень - {z.get_level()} | Здоровье - {z.get_health()} | Опыт - {z.get_experience()}\n")

print(f"Добавлено {z.set_experience(62)} баллов опыта\n")

print(f"Уровень - {z.get_level()} | Здоровье - {z.get_health()} | Опыт - {z.get_experience()}\n")

print(f"Добавлено {z.set_experience(155)} баллов опыта\n")

print(f"Уровень - {z.get_level()} | Здоровье - {z.get_health()} | Опыт - {z.get_experience()}\n")

print(f"Добавлено {z.set_experience(223)} баллов опыта\n")

print(f"Уровень - {z.get_level()} | Здоровье - {z.get_health()} | Опыт - {z.get_experience()}\n")