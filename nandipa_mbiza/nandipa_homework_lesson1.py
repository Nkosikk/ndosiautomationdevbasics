# Capture information of 2 users. This information includes their name, age and height (in cm).
# Display each user's information in a sentence format.
# Then calculate and display the total combined height of both users.

name1 = input("Enter first user's name: ")
age1 = input("Enter first user's age: ")
height1 = input("Enter first user's height: ")
print()

name2 = input("Enter second user's name: ")
age2 = input("Enter second user's age: ")
height2 = input("Enter second user's height: ")
print()
height1 = int(height1)
height2 = int(height2)

print(f"First user's name is {name1} and age is {age1} and height is {height1}.")
print(f"Second user's name is {name2} and age is {age2} and height is {height2}.")

print(f"The total height for both users is {height1 + height2}.")
