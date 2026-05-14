user_data = { #Dict store multiple values on one variable
    'name' : 'Mary',
    'age' : 32,
    'height' : 21.9,
}
#key value pairs

print(user_data)
print(type(user_data)) #dict

print()

del user_data['NAME']
print(user_data) #KeyError: 'NAME'