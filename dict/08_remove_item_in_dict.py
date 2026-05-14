user_data = { #Dict store multiple values on one variable
    'name' : 'Mary',
    'age' : 32,
    'height' : 21.9,
}
#key value pairs

print(user_data)
print(type(user_data)) #dict

print()

print('removing name from dict')
del user_data['name'] #removing name from dict
print(user_data)

