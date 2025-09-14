import pickle

class Zoo_Aggr:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        self.attendants = []

#***************** Save & Retrieve the Zoo ************************************************
    def save_zoo(self):
        """сохранение в: zoo_state.pkl (binary) и zoo_info.txt для людей"""
        # 1. Для программы (бинарный pickle)
        with open('zoo_state.pkl', 'wb') as f:
            pickle.dump(self, f)

        # 2. Для людей (txt)
        with open('zoo_info.txt', 'w', encoding='utf-8') as f:
            f.write(f"Зоопарк: {self.name}\n")
            f.write(f"Адрес: {self.address}\n")
            f.write(f"Животных: {len(self.animals)}\n")
            f.write(f"Сотрудников: {len(self.attendants)}\n\n")

            f.write("СПИСОК ЖИВОТНЫХ:\n")
            for animal in self.animals:
                f.write(f"- {animal.name} ({animal.species}), {animal.age} лет\n")

            f.write("\nСПИСОК СОТРУДНИКОВ:\n")
            for attendant in self.attendants:
                f.write(f"- {attendant.name}: {attendant.position}, {attendant.pay} руб.\n")

    @classmethod
    def load_zoo(cls):
        """Загрузка прошлого зоопарка из zoo_state.pkl"""
        with open('zoo_state.pkl', 'rb') as f:
            return pickle.load(f)
#********************************************************************************************

    class ZooAnimal:  # Вложенный класс - Э тока внутри Zoo_Aggr
        def __init__(self, zoo, name, species, age):
            self.zoo = zoo  # ссылка на родительский зоопарк
            self.name = name
            self.species = species
            self.age = age

        def __repr__(self):  # ← метод форматирования при выводе списка
            return f"{self.name} ({self.species}) {self.age} лет\n"

    class ZooAttendant:
        def __init__(self, zoo, name, position, pay):
            self.zoo = zoo
            self.name = name
            self.position = position
            self.pay = pay

        def __repr__(self):  # ← тоже
            return f"{self.name} ({self.position}) з/п: {self.pay} руб.\n"
#*************************************************************

    def add_animal(self, name, species, age):
        animal = self.ZooAnimal(self, name, species, age)
        self.animals.append(animal)
        print(f'Ж {animal.name}, ({animal.species}) -- добавлено')
        return animal

    def add_attendant(self, name, position, pay):
        if 'смотритель' in position.lower():
            attendant = self.ZooKeeper(self, name, position, pay)
        elif 'ветеринар' in position.lower():
            attendant = self.ZooVet(self, name, position, pay)
        else:
            attendant = self.ZooAttendant(self, name, position, pay)

        self.attendants.append(attendant)
        print(f'сотрудник {attendant.name}, {attendant.position} -- добавлен')
        return attendant

# HW i.5 -- создать классы для сотрудников
    class ZooKeeper(ZooAttendant):
        def __init__(self, zoo, name, position='смотритель', pay=50000):
            super().__init__(zoo, name, position, pay)

        def feed_animals(self):
            #   for animal in animals:
            print(f'{self.name} кормит животных')

    class ZooVet(ZooAttendant):
        def __init__(self, zoo, name, position='ветеринар', pay=70000):
            super().__init__(zoo, name, position, pay)

        def heeal_animal(self):
            #   for animal in animals:
            print(f'{self.name} лечит больное животное')

#===================== Testing =====================================

# Загружаем сохраненное сост-е
the_zoo = Zoo_Aggr.load_zoo()

# Проверяем:
print(f"Загружен зоопарк: {the_zoo.name}")
print(f"Животных: {len(the_zoo.animals)}")
print(f"Сотрудников: {len(the_zoo.attendants)}")

print(the_zoo.animals)
print(the_zoo.attendants)
'''

the_zoo = Zoo_Aggr("Пионерский", 'Пятисобачий пер., 5')
animal1 = Zoo_Aggr.ZooAnimal(zoo=the_zoo, name='Кеша', species='Птеродактиль', age=20000) # создаёт, но в [] не ++
the_zoo.animals.append(animal1)  # - тогда + вот так

the_zoo.add_animal('Зайка','зайки', 1 )
the_zoo.add_attendant('Иван Иваныч', 'директор', 100000)

for animal in the_zoo.animals:
    print(animal.name)
for attendant in the_zoo.attendants:
    print(attendant.name, attendant.position, attendant.pay)
#zookeeper1 = the_zoo.ZooKeeper(the_zoo, 'Вася', 'Chief ZooKeeper', 70000 )
#the_zoo.add_attendant(the_zoo.ZooKeeper(the_zoo, 'Вася', 'Chief ZooKeeper', 70000)
#zookeeper1.feed_animals()
#==================== for extra classes ============================
zk1 = the_zoo.add_attendant('Вася', 'смотритель', 55000)
vet = the_zoo.add_attendant('Боря', 'ветеринар', 73000)

zk1.feed_animals()
vet.heeal_animal()

print(the_zoo.attendants)
for attendant in the_zoo.attendants:
    print(attendant.name,'\t', attendant.position,'\t', attendant.pay)
'''
the_zoo.save_zoo()
