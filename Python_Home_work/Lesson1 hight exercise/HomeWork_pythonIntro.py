""" Intro to Python
Capture information of 2 users. This information includes their ame, age and height (in cm).
Display each user&#039;s information in a sentence format.
Then calculate and display the total combined height of both users.

Advanced User Profile Manager (Python)
Push your completed Lesson 1 homework to your own Git repo on the main branch.
Create a new branch called lesson3-homework.

Update your lesson 1 homework to capture information of 2 users. This information includes their name, age and height (in cm).
Make use of list and dictionaries.
Validation of user input is optional.
Display each user&amp;#039;s information in a sentence format (make use of loops).
Then calculate and display the total combined height of both users (make use of a function).

Commit and push your code, and create a Pull Request (PR) into main.



'lession 1'
print("************** lesson1-homework using the variables: **************\n")

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

from xml.dom.minidom import ProcessingInstruction

from lesson1.Homework import total_height

"lesson3-homework"

print("************** lesson3-homework using the List: **************")
name = input("Please Enter your name: ")
age = int(input("Please Enter your age: "))
height = float(input("Please Enter your height: "))

userLs = [name,age,height]

print(f'your name is : {userLs[0]}, your age is : {userLs[1]}, the height is: {userLs[2]:.2f} in cm')

name2 = input("Please Enter your name: ")
age2 = int(input("Please Enter your age: "))
height2 = float(input("Please Enter your height: "))

userLs2 = [name2,age2,height2]

print(f'your name is : {userLs2[0]}, your age is : {userLs2[1]}, the height is: {userLs2[2]:.2f} in cm')
total_height =(userLs[2]+userLs2[2])

print(f" the combined weight for {userLs[0]} and {userLs[0]} is {total_height:.2f} in cm")
print("\n")

"""
from lesson1.Homework import total_height

print("************** lesson3-homework end of List : **************\n")

username = input("Please Enter your name: ")
userage = int(input("Please Enter your age: "))
userheight = float(input("Please Enter your height: "))

myDict = {"name": username, "age": userage, "height": userheight}


username1 = input("Please Enter your name: ")
userage1 = int(input("Please Enter your age: "))
userheight1 = float(input("Please Enter your height: "))

myDict1 = {"name": username1, "age": userage1, "height": userheight1}

print(f"This is the details for the first user: {myDict}")
print(f"This is the details for the second user: {myDict1}")

newDict = {"user": [username,userage,userheight]}
newDict1 = {"user1": [username1,userage1,userheight1]}

total_height = newDict["user"][2] + newDict1["user1"][2]

print(f"This is this is the new dictionary\n")
print(f"This is the details for the first user: {newDict}\n")
print(f"This is the details for the second user: {newDict1}\n")

print(f"The total combined height is : {total_height: .2f}\n")

"Looping"

'looping for the first user'
for index, info in enumerate(newDict["user"]):
    if index == 0:
        print(f"The users name's is :{info}\n")
    elif index == 1:
        print(f"The user's age is :{info}\n")
    elif index == 2:
        print(f"The user's height is :{info}\n")

for index, info in enumerate(newDict1["user1"]):
    if index == 0:
        print(f"The users name's is :{info}\n")
    elif index == 1:
        print(f"The user's age is :{info}\n")
    elif index == 2:
        print(f"The user's height is :{info}\n")
