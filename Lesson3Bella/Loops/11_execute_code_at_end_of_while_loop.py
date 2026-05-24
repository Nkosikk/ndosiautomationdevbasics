number = 1

while number < 10:
    print(f'Forever {number}')

    if number > 10:
        break   #stops a loop

    number = number + 1

else: #execute after the normal loop
    print('Done looping')