user_data = {
    'name': 'Mary',
    'age': 32,
    'height': '21.9'
}
#key-value pairs


print(user_data)
print(type(user_data)) #dict

print()

print('Remove name from dictionary')
del user_data['name']  #removing name from dict
print(user_data)