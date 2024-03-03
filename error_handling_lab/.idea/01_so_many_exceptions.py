# numbers_list = int(input()).split(", ")
# input()).split(", ") returns a list
# need to use comprehension to turn the
# input to intgeres
numbers_list = [int(x) for x in input().split(", ")]
result = 1

# for i in range(numbers_list):
# The range should be in the length of the listnot the list itself
for i in range(len(numbers_list)):
    # number = numbers_list[i+1]
    # Should start from index 0
    number = numbers_list[i]
    # if number <= 5
    # SyntaxError: expected ':'
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

# print(total)
# "total" is not defined, should use "result"
print(result)
