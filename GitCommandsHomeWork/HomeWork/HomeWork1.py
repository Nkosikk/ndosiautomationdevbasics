#user1infor
UserName1 = input('Enter name: ')
UserAge1 = input('Enter age: ')
UserHeight1 = input('Enter height: ')

print(f'Your name is {UserName1} ,you are {UserAge1} years old and your height is {UserHeight1} centimeters')

#user2infor
UserName2 = input('Enter name: ')
UserAge2= input('Enter age: ')
UserHeight2 = input('Enter height: ')

print(f'Your name is {UserName2} ,you are {UserAge2} years old and your height is {UserHeight2} centimeters')

#HeightsCombined
UserHeight1 = float(UserHeight1)
UserHeight2 = float(UserHeight2)

totalHeight = UserHeight1 + UserHeight2
print(f'Total Height Combined is {totalHeight} centimeters')
