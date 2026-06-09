#Update your lesson 1 homework to capture information of 2 users. This information includes their name, age and height (in cm).
#Make use of list and dictionaries.
#Validation of user input is optional.
#Display each user's information in a sentence format (make use of loops).
#Then calculate and display the total combined height of both users (make use of a function).

#Step 1: Create a list of users
users = [
    {
        "name": "Peter",
        "age": 19,
        "height": 156
    },
    {
        "name": "Maggy",
        "age": 20,
        "height": 171
    }
]

#Step 2: Use a loop to display the information
for user in users:
    print(
        f"{user['name']} is {user['age']} years old and is {user['height']} cm tall."
    )

#Step 3: Create a function
def calculate_total_height(users):
    total_height = 0

    for user in users:
        total_height += user["height"]

    return total_height


combined_height = calculate_total_height(users)

print(f"Total combined height: {combined_height} cm")