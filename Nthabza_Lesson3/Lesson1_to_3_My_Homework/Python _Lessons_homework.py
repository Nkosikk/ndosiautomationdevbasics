#Update your lesson 1 homework to capture information of 2 users. This information includes their name, age and height (in cm).
#Make use of list and dictionaries.
#Validation of user input is optional.
#Display each user's information in a sentence format (make use of loops).
#Then calculate and display the total combined height of both users (make use of a function).

users = []

for i in range(2):
    print(f"\nEnter details for User {i + 1}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height (cm): "))

    user = {
        "name": name,
        "age": age,
        "height": height
    }

    users.append(user)


for user in users:
    print(
        f"{user['name']} is {user['age']} years old and is {user['height']} cm tall."
    )


def calculate_total_height(users):
    total_height = 0

    for user in users:
        total_height += user["height"]

    return total_height


total_height = calculate_total_height(users)

print(f"\nTotal combined height: {total_height} cm")
