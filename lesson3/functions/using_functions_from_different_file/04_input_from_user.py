# Option 2: Importing a single function
# import calculations
from calculations import add, subtract


num1 = int(input('Input number 1:'))
num2 = int(input('Input number 2:'))

# answer = calculations.add(10, 20)
answer = add(num1, num2)
print(answer)

answer1 = subtract(num1, num2)
print(answer1)


