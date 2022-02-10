def sum_digits(number):
    str_number = str(number)
    sum_of_number = 0
    for num in str_number.strip("-"):
        sum_of_number += int(num)
    return sum_of_number