""" Intro to Python
Capture information of 2 users. This information includes their ame, age and height (in cm).
Display each user&#039;s information in a sentence format.
Then calculate and display the total combined height of both users.
"""

print("Welcome to you and your friend's Height calculator please enter your in cm! ")

name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))
height = float(input("Please Enter your height: "))
print(f" Ok to confirm your details: \n Your name is : {name}\n Your age is : {age} \n Your height is  : {height} in cm")
print("Thank you now let get your friend's name, age and height in cm!\n")

name2 = input("what is your friends name: ")
age2 = int(input("Please Enter your age: "))
height2 = float(input("Please Enter your height: "))

print(f"Ok to confirm your details: \n Your name is : {name2}\n Your age is : {age2} \n Your height is  : {height2} in cm\n")
totalHieght: float = height + height2
print(f"Your height is  : {height} and your friends height is {height2} in cm, your combined height is { totalHieght:.2f} in cm WOW! ")
