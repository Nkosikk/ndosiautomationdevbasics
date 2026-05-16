# First user
name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
hight = float(input('Please enter your hight in cm: '))
print()
shopping_list1 = []
shopping_list1.insert(0, input('Please enter your shopping list: '))
shopping_list1.insert(1, input('Please enter your shopping list: '))
shopping_list1.insert(2, input('Please enter your shopping list: '))
print()

# Second user
name2 = input('Please enter your name: ')
age2 = int(input('Please enter your age: '))
hight2 = float(input('Please enter your hight in cm: '))
print()

first_user = {}
first_user['name'] = name
first_user['age'] = age
first_user['hight'] = hight

second_user = {}
second_user['name'] = name2
second_user['age'] = age2
second_user['hight'] = hight2

print(first_user)
print(shopping_list1)
print()
print(second_user)