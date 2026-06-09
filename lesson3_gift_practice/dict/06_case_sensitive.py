user_data = { #Dict store multiple values on one variable
    'name' : 'Mary',
    'age' : 32,
    'height' : 21.9,
    'name' : 'Peter'
}
#key value pairs
print(user_data)
print(type(user_data))

print()

print(user_data['NAME']) #KeyError: 'NAME' : case sensitive


