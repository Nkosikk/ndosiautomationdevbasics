# Function to calculate total height
def calculate_total_height(users):
    total_height = 0

    for user in users:
        total_height += user["height"]

    return total_height


# List containing dictionaries for 2 users
users = []

# Capture information for 2 users
for i in range(2):
    print(f"\nEnter details for User {i + 1}")

    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height in cm: "))

    user = {
        "name": name,
        "age": age,
        "height": height
    }

    users.append(user)


# Display user information
print("\n--- User Information ---")

for user in users:
    print(
        f"{user['name']} is {user['age']} years old "
        f"and has a height of {user['height']} cm."
    )


# Calculate total combined height
total_height = calculate_total_height(users)

print(f"\nTotal combined height: {total_height} cm")