class Hero:

    def __init__(self):
        self.coins = []
        self.gold_equivalent = 0

    def get_money(self):
        for pocket in self.coins:
            if pocket.material == 'diamond':
                self.gold_equivalent += pocket.value * 100
            if pocket.material == 'gold':
                self.gold_equivalent += pocket.value
            if pocket.material == 'silver':
                self.gold_equivalent += pocket.value / 10
            if pocket.material == 'bronze':
                self.gold_equivalent += pocket.value / 100
        return self.gold_equivalent


class Coin:
    def __init__(self, value, material):
        self.value = value
        self.material = material


hero = Hero()

coins = [Coin(5, "gold"), Coin(35, "silver"), Coin(78, "bronze"), Coin(1, "diamond")]

hero.coins = coins

print("В пересчёте на золото у героя", hero.get_money(), "монет")

