for name in range(1, 16, 2):
    print(name)


print('-----------------------------')

for name in range(1, 16, 2):
    if 5 <= name and name <= 10:
        continue
    print(name)
