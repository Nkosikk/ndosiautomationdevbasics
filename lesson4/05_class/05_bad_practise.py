class User:
    # Constructor (ctor)
    def __init__(self, name: str):
        self.name = name

    def add_age(self, age: int):
        self.age = age

    def print_user_data(self):
        print(f'My name is {self.name}')




user = User('Mary')  # object
print(f'{user.name} is {user.age} years old')

user.add_age(32)

print(f'{user.name} is {user.age} years old')


