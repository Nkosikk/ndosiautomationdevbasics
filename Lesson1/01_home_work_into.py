name1 = input('Enter name1')
age1 = int(input('Enter age1'))
height1 = float(input('Enter height1'))
name2 = input('Enter name2')
age2 = int(input('Enter age2'))
height2 = float(input('Enter height2'))

print(name1, age1, height1 * 100)
print(name2, age2, height2 * 100)

total_height: float = height1 + height2
print(f'Total height combined is {total_height * 100} in cm')
