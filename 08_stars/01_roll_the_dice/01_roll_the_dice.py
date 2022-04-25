import random


class Dice:
    def __init__(self, sides_count):
        self._sides_count = int(sides_count)

    def dice_throw(self):
        dice_throw = random.randint(1, self._sides_count)
        self.set_history(dice_throw)
        return dice_throw

    def get_history(self, last_dices_count):
        with open('history.txt', 'r', encoding='utf-8') as file:
            return ", ".join(file.read().strip().split(" ")[-last_dices_count:])

    def set_history(self, dice_throw):
        with open('history.txt', 'a', encoding='utf-8') as file:
            file.write(str(dice_throw) + " ")


while True:
    sides = input("Введите кол-во граней кубика [4, 6, 8, 10, 20, 100]\n")
    while sides not in ['4', '6', '8', '10', '20', '100']:
        sides = input("Введите кол-во граней кубика [4, 6, 8, 10, 20, 100]\n")

    dice = Dice(sides)

    print("Выпала цифра: " + str(dice.dice_throw()))
    print("История: " + dice.get_history(4) + "\n")
