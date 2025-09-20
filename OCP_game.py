# HWOB04 - Game to demo OCP
class Fighter:
    def __init__(self, name, strength=10):
        self.name = name
        self.strength = strength
        self.weapon = None      # инициализирует weapon

    def pickup_weapon(self, weapon='sword'):
        self.weapon = weapon
        return self.weapon


class Monster:
    def __init__(self, name, strength=20):
        self.name = name
        self.strength = strength

    def change_strength(self, strength):
        self.strength = strength
        return self.strength






