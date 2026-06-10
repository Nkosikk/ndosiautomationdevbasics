def print_even_numbers(num_list: list):
    for number in num_list:
        if number % 2 == 0:
            print(number)

numbers = [10, 20, 30, 34, 54, 31,1,8,7]

print_even_numbers(numbers)
