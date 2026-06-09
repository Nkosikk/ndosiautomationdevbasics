for name in range(1, 20, 2):   # (start, stop not inclusive, step)
    # if name == 5 or name == 7:
    #     continue
    if 5 <= name <= 15:  # skip from 5 to 15 (included)
        continue

    print(name)
