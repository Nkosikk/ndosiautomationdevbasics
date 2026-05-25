# user1's information
name1 = input("Enter user1's name: ")
age1 = int(input("Enter user1's age: "))
height1 = float(input("Enter user1's height in cm: "))

# user2's information
name2 = input("Enter user2's name: ")
age2 = int(input("Enter user2's age: "))
height2 = float(input("Enter user2's height in cm: "))

# Display user information
print(f"{name1} is {age1} years old and {height1} cm tall.")
print(f"{name2} is {age2} years old and {height2} cm tall.")

# Calculate total combined height
total_height = height1 + height2

# Display total height
print(f"The total combined height is {total_height} cm.")
