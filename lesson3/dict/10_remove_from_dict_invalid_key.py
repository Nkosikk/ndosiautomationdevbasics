user_data = {
    'name': 'Mary',
    'age': 32,
    'height': 21.9
}
# key-value pairs


print(user_data)
print(type(user_data))  # lesson3_gift_practice


print()

print('Removing gender from lesson3_gift_practice')
del user_data['gender']  # removing gender from lesson3_gift_practice
# Error: KeyError
print(user_data)

