# User-Accounts-Manaagement-Sysyem - USAM

class User:
    def __init__(self, ID, name, access = 'user'):
        self.ID = ID
        self.name = name
        self.access = access

class Admin(User):
    def __init__(self, ID, name):
        super().__init__(ID, name, 'admin')
        self.users = []

    def add_user(self, name):
        user_ID = len(self.users) + 1
        new_user = User(user_ID, name, 'user')
        self.users.append(new_user)
        print(f'Added user ID: {user_ID} {name}')

# testing

admin = Admin(1, 'Admin')
admin.add_user('Вася')
admin.add_user('Коля')

for user in admin.users:
    print (user.ID, user.name)









