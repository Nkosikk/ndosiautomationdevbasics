user_data = { #Dict store multiple values on one variable
    'name' : 'Mary',
    'age' : 32,
    'height' : 21.9,
}
#key value pairs
print(user_data)
print(type(user_data))

print()

print('Update height')
user_data['height'] = 20
print(user_data)
