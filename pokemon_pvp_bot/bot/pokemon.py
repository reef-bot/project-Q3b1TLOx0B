import random

class Pokemon:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.hp = self.calculate_hp()
        self.attack = self.calculate_attack()
        self.defense = self.calculate_defense()
        self.speed = self.calculate_speed()

    def calculate_hp(self):
        return random.randint(50, 100) + self.level * 2

    def calculate_attack(self):
        return random.randint(10, 20) + self.level

    def calculate_defense(self):
        return random.randint(5, 15) + self.level

    def calculate_speed(self):
        return random.randint(5, 15) + self.level