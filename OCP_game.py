# HWOB04 - Game to demo OCP
from abc import ABC, abstractmethod
#=========================WEAPONS==========================================================
class Weapon(ABC):
    @abstractmethod
    def use_weapon(self):
        pass
    def _check_health(self, target):
        if target.health <= 0:
            print(f'{target.name} погиб...')

class Sword(Weapon):
    def __init__(self):
        self.name = "меч"
        self.damage = 2
    def use_weapon(self, attacker, target):
        target.health -= self.damage
        print(f"{attacker.name} колет: Ыы...ыыы! - минус 2 пункта здоровья у {target.name}, осталось: {target.health}")
        self._check_health(target)

class Gun(Weapon):
    def __init__(self):
        self.name = "ружьё"
        self.damage = 5
    #self.weapon = 'ружьё'
    def use_weapon(self, attacker, target):
        target.health -= self.damage
        print(f"{attacker.name} жах!: Ууууу...! - минус 5 пунктов здоровья у {target.name}, осталось: {target.health}")
        self._check_health(target)
#=========================FIGHTERS==========================================================
class Fighter:
    def __init__(self, name, strength=10):
        self.name = name
        self.strength = strength
        self.weapon = Sword()      # получит экземпляр меча при рождении

    def pickup_weapon(self, weapon):
        self.weapon = weapon
        print(f'{self.name} взял {self.weapon.name}')
        return self.weapon

    def use_weapon(self, target):
        self.weapon.use_weapon(self, target)

class Monster:
    def __init__(self, name, health=20, strength=30):
        self.name = name
        self.strength = strength
        self.health = health

    def change_health(self, health):
        self.health = health
        return self.health

f1 = Fighter('Вася')
m1 = Monster('Кака')
w1 = Sword()
w2 = Gun()
f1.use_weapon(m1)
f1.use_weapon(m1)
f1.use_weapon(m1)
f1.pickup_weapon(w2)
f1.use_weapon(m1)
f1.use_weapon(m1)
f1.use_weapon(m1)

