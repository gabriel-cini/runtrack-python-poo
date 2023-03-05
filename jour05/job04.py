def max_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        first_number = numbers[0]
        max_of_rest = max_number(numbers[1:])
    return first_number if first_number > max_of_rest else max_of_rest
max_number([2, 7, 1, 8, 4])
8
max_number([5, 3, 1, 6, 4, 7])
7
max_number([9])
9
