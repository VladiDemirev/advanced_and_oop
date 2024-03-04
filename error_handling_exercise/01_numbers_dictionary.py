numbers_dictionary = {}

line = input()

while line != "Search":
    number_as_string = line

    # Added try-except block to catch ValueError
    try:
        number = int(input())
    except ValueError:
        print("The variable number must be an integer")
    else:
        numbers_dictionary[number_as_string] = number

    # Added missing input command
    line = input()

line = input()

while line != "Remove":
    searched = line

    # Added try-except block to catch KeyError
    try:
        print(numbers_dictionary[searched])
    except KeyError:
        print("Number does not exist in dictionary")

    # Added missing input command
    line = input()

line = input()

while line != "End":
    searched = line

    # Added try-except block to catch KeyError
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")

    # Added missing input command
    line = input()

print(numbers_dictionary)
