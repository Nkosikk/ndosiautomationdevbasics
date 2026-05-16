class User:
    # Constructor (ctor)
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_user_data(self):
        print(f'My name is {self.name}')


user = User('Mary', 32)  # object
print(f'{user.name} is {user.age} years old')


