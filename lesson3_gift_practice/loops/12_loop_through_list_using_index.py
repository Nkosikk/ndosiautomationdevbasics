numbers = [10, 20, 30, 40, 50]

for index in range(2, len(numbers)):
     print(f'index -> {index}, value -> {numbers[index]}')

print('------------------')

users = [
     {
          'name': 'Mary'
     },
     {
          'name': 'Peter'
     }
]

for user in users:
     print(user)
     print(f'You are {user['name']}')

