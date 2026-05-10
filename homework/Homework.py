get_user1_name = input('Enter user1 name: ') #Enter and store user1 name
get_user1_age = input('Enter user1 age: ') #Enter and store user1 age
user1_age = int(get_user1_age) #Convert user1 age string to int
get_user1_height = input('Enter user1 height: ') #Enter and store user1 age
user1_height = float(get_user1_height) #Enter and store user1 height
user1_height_in_cm = user1_height * 2.54

print(f'user1 name is {get_user1_name}, {user1_age} years old, and {user1_height_in_cm} cm tall') #print user1 details
print()

get_user2_name = input('Enter user2 name: ') #Enter and store user2 name
get_user2_age = input('Enter user2 age: ') #Enter and store user2 age
user2_age = int(get_user2_age) #Convert user2 age string to int
get_user2_height = input('Enter user2 height: ') #Enter and store user2 age
user2_height = float(get_user2_height) #Enter and store user2 height
user2_height_in_cm = user2_height * 2.54

print(f'user2 name is {get_user2_name}, {user2_age} years old, and {user2_height_in_cm} cm tall') #print user2 details
print(f'Total combined height for both users, {user1_height} inches tall + {user2_height} inches tall is {user1_height_in_cm + user2_height_in_cm} cm.')