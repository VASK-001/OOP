# User-Accounts-Management-System - USAM

class User:
    def __init__(self, ID, name, access = 'user'):
        self.ID = ID
        self.name = name
        self.access = access

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name, 'admin')
        self.__users = []   # <<<< закрытый список пользователей

    def __add_user(self, name):
        print(f'Вызван закрытый метод __add_user для :{name}')
        user_ID = len(self.__users) + 1
        new_user = User(user_ID, name, 'user')
        self.__users.append(new_user)
        print(f'User added: {user_ID} {name}')
        return new_user

    def add_user_public(self, name):
        print(f"Админ {self.name} добавляет пользователя: {name}")

        # Проверка прав (админ ли ты, друже)
        if self.access != 'admin':
            print("Недостаточно прав!")
            return None

        # Вызов закрытого метода
        new_user = self.__add_user(name)
        print("Пользователь добавлен через публичный интерфейс!\n")
        return new_user

    def show_users(self):
        """Публичный метод для показа пользователей"""
        print(f"\n=== Список пользователей админа {self.name} ===")
        for user in self.__users:
            print(user.ID, user.name, user.access)

# testing *********************************************************
print("=== 1. Создаем админа ===")
admin = Admin(1, 'Главный Админ')
print(f"Создан: ID: {admin.ID}, Name: {admin.name}, Access: {admin.access}")

print("\n=== 2. Правильный вызов через публичный метод ===")
admin.add_user_public('Вася')
admin.add_user_public('Коля')

print("=== 3. Попытка вызвать приватный метод напрямую ===")
try:
    admin.__add_user('Хакер')  # Это вызовет ошибку!
except AttributeError as e:
    print(f"ОШИБКА: {e}")
    print("Приватный метод нельзя вызвать напрямую!\n")

print("=== 4. Показ пользователей через публичный метод ===")
admin.show_users()
# ******************************************************************

# old testing =====================================
'''
admin = Admin(1, 'Admin')
admin.add_user('Вася')
admin.add_user('Коля')

for user in admin.users:
    print (user.ID, user.name)
================================================='''







