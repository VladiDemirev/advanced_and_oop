# numbers_list = int(input()).split(", ") - ValueError: invalid literal for int() with base 10: '2, 5, 10'
# Wrong way to convert the string to integers.
# Can do this by using list comprehension.
numbers_list = [int(x) for x in input().split(", ")]
result = 1

# for i in range(numbers_list): - TypeError: 'list' object cannot be interpreted as an integer.
# Should iterate through the length of the list.
for i in range(len(numbers_list)):
    # number = numbers_list[i + 1] - IndexError: list index out of range
    number = numbers_list[i]
    # if number <= 5 - SyntaxError: expected ':'
# Added missing semicolon at the end.
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

# print(total) - NameError: name 'total' is not defined
# Can use the declared the variable 'result'
print(result)
