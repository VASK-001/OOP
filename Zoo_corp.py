class Zoo_Aggr:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.animals = []
        self.attendants = []

    class ZooAnimal:  # Вложенный класс - Э тока внутри Zoo_Aggr
        def __init__(self, zoo, name, species, age):
            self.zoo = zoo  # ссылка на родительский зоопарк
            self.name = name
            self.species = species
            self.age = age

    class ZooAttendant:
        def __init__(self, zoo, name, position, pay):
            self.zoo = zoo
            self.name = name
            self.position = position
            self.pay = pay
    #*************************************************************

    def add_animal(self, name, species, age):
        animal = self.ZooAnimal(self, name, species, age)
        self.animals.append(animal)
        print(f'Ж {animal.name}, ({animal.species}) -- добавлено')
        return animal

    def add_attendant(self, name, position, pay):
        attendant = self.ZooAttendant(self, name, position, pay)
        self.attendants.append(attendant)
        print(f'сотрудник {attendant.name}, {attendant.position} -- добавлен')
        return attendant

the_zoo = Zoo_Aggr("Пионерский", 'Пятисобачий пер., 5')
animal1 = Zoo_Aggr.ZooAnimal(zoo=the_zoo, name='Кеша', species='Птеродактиль', age=2000) # создаёт, но в [] не ++
the_zoo.animals.append(animal1)  # - тогда + вот так

the_zoo.add_animal('Зайка','зайки', 1 )
the_zoo.add_attendant('Иван Иваныч', 'директор', 100000)

for animal in the_zoo.animals:
    print(animal.name)
for attendant in the_zoo.attendants:
    print(attendant.name, attendant.position, attendant.pay)
