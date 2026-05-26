def print_even_numbers(num_list: list):
    print(num_list)
    print(len(num_list))
    # TODO: finish this off...
    for num in num_list:
        if num % 2 == 0:
            print(num)

numbers = [10, 20, 30, 34, 54, 31]
print_even_numbers(numbers)