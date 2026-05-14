import json

with open('user.json', 'r') as file:
    user_data = json.load(file)
    print(user_data)
    print(type(user_data))

    print(f"Name is {user_data['name']}")
