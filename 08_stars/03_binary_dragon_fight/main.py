class Dragon:

    _powers_of_two = []
    for i in range(1, 11):
        _powers_of_two.append(2 ** i)

    _is_alive = True

    def __init__(self, name, color, health=100):
        self._name = name
        self._color = color
        self._health = health

    def __repr__(self):
        return f"\nРодился дракоша {self._name} цвета {self._color} со здоровьем {self._health}\n"

    def get_health(self):
        if self._is_alive:
            return f"У {self._name} {self._health} здоровья\n"
        else:
            return f"{self._name} мёртв\n"

    def bite(self, bite=10):
        if self._is_alive:
            self._health += bite
            return f"Кусь на +{bite} к здоровью\n" \
                   f"{self.get_health()}"
        else:
            return f"Кусь невозможен, {self._name} мёртв\n"

    def damage(self, damage=10):
        if self._is_alive and damage in self._powers_of_two:
            h = []
            for k in self._powers_of_two:
                if self._health > k:
                    h.append(self._powers_of_two[self._powers_of_two.index(k) + 1]) # так не хорошо делать, но пока так ))
            self._health = h[-1]
            return f"Боги благосклонны к {self._name}\n" \
                   f"Вместо урона {damage} его здоровье восстанавливается до {self._health}\n"
        elif not self._is_alive:
            return f"{self.get_health()}Не пинайте лежачего\n"
        elif damage > self._health:
            self._health = 0
            self._is_alive = False
            return f"{self._name} получил {damage} урона и умер\n"
        elif self._is_alive:
            self._health = self._health - damage
            return f"{self._name} получил {damage} урона\n" \
                   f"{self.get_health()}"

    def resurrect(self, health=50):
        self._health = 50
        self._is_alive = True
        return f"Боги благосклонны к {self._name}\n" \
               f"И воскрешают его со здоровьем {health}\n"


d = Dragon("DragonFly", "indigo")

print(d)

print(d.bite(10))

print(d.damage(16))

print(d.damage(111))

print(d.damage(1024))

print(d.bite(50))

print(d.bite())

print(d.damage(15))

print(d.bite())

print(d.damage())

print(d.bite(25))

print(d.bite(36))

print(d.damage(4))

print(d.damage(1023))

print(d.damage(16))

print(d.resurrect(50))

print(d.bite())

print(d.damage(14))

print(d.damage(145))

print(d.bite())

print(d.damage(145))

print(d.resurrect(100))