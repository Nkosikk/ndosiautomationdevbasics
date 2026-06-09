user_data = { #Dict store multiple values on one variable
    'name' : 'Mary',
    'age' : 32,
    'height' : 21.9,
}
#key value pairs
print(user_data)
print(type(user_data))

print()

print('Get user name')
print(user_data['name'])

#print(user_data['nmea']) #KeyError