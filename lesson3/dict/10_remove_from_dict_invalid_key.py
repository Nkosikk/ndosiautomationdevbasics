user_data = {
    'name': 'Mary',
    'age': 32,
    'height': 21.9
}
# key-value pairs


print(user_data)
print(type(user_data))  # dict


print()

print('Removing gender from dict')
del user_data['gender']  # removing gender from dict
# Error: KeyError
print(user_data)

