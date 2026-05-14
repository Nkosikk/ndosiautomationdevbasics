class User:
    # Constructor (ctor)
    def __init__(self, name: str):
        self.name = name

    def print_user_data(self):
        print(f'My name is {self.name}')




user = User('Mary')  # object
user.print_user_data()



user2 = User('Peter')  # object
user2.print_user_data()
