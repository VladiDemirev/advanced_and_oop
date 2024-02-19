def even_numbers(function):
    def wrapper(nums):
        # def wrapper(*args, **kwargs):
        # result = function(*args, **kwargs)
        # even_numbers = [num for num in result if num % 2 == 0]
        even_numbers = [num for num in nums if num % 2 == 0]
        return even_numbers

    return wrapper


#  Test Code

@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
