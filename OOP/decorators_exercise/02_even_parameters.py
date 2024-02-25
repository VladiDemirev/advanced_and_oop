def even_parameters(func):
    def wrapper(*args):
        if any(not isinstance(el, int) or el % 2 != 0 for el in args):
            return "Please use only even numbers!"
        # for el in args:
        #   if not isinstance(el, int) or el % 2 != 0:
        #     return "Please use only even numbers!"
        result = func(*args)
        return result

    return wrapper


#  Test Code

@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
print()


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
