# Capture information for User 1
name1 = input("Enter the name of User 1: ")
age1 = int(input("Enter the age of User 1: "))
height1 = float(input("Enter the height of User 1 (in cm): "))

# Capture information for User 2
name2 = input("\nEnter the name of User 2: ")
age2 = int(input("Enter the age of User 2: "))
height2 = float(input("Enter the height of User 2 (in cm): "))

# Display user information
print(f"\n{name1} is {age1} years old and is {height1} cm tall.")
print(f"{name2} is {age2} years old and is {height2} cm tall.")

# Calculate total combined height
total_height = height1 + height2

# Display total height
print(f"\nThe total combined height of both users is {total_height} cm.")