# Capture information for User 1
user1_data= {
    'name': 'Mary',
    'age': 32,
    'height': 21
}
# key-value pairs


print(user1_data)
print(type(user1_data))

print()

# Capture information for User 2
user2_data = {
    'name': 'Jane',
    'age': 30,
    'height': 20
}
# key-value pairs


print(user2_data)
print(type(user2_data))

print()

# Display user information

print(f'You are {user1["name"]} and {user1["age"]} years old and is {user1["height"]}')
print(f'You are {user2["name"]} and {user2["age"]} years old and is {user2["height"]}')

print()

# Calculate and display total combined height

def add(num1: int, num2: int):
    return num1 + num2
sum_of_numbers = add(num1: 21, num2:20)
print(sum_of_numbers)
