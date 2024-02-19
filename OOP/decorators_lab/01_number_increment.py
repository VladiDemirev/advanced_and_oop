def number_increment(numbers):
    def increase():
        # incremented_numbers = [num + 1 for num in numbers]
        # return incremented_numbers
        return [num + 1 for num in numbers]

    return increase()


#  Test Code

print(number_increment([1, 2, 3]))
