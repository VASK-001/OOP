# Программа Zoo
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('Ж издаёт характерный звук')

    def eat(self):
        print('Ж ест')

class Bird(Animal):
    def __init__(self, name, age, food = 'крокодила'):
        super().__init__(name, age)
        self.food = food

    def eat(self):
        print(f'{self.name} ест {self.food}')

    def make_sound(self):
        print('КАРРР!')


animal = Animal('Moo', 15)
animal.eat()
animal.make_sound()
print(f'{animal.name} {animal.age}')

bird = Bird('Птеро', 25 )
bird.eat()
bird.make_sound()

class Dog(Animal):
    def __init__(self, name = 'Шарик', age = 1, food = 'Матроскина', voice = 'Гав!'):
        super().__init__(name, age)
        self.name = name
        self.age = age
        self.food = food
        self.voice = voice

    def eat(self):
        print(f'{self.name} ест {self.food}')

    def make_sound(self):
        print(f'{self.name} говорит {self.voice}')

print('***********************')
dog = Dog()
dog.eat()
dog.make_sound()
print('***********************')
dog2 = Dog(name='Дик',food='тушёнку', voice='Рррр-гав!')
dog2.eat()
dog2.make_sound()


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

print('-------------------')
animals = [dog, dog2, bird]
animal_sound(animals)
