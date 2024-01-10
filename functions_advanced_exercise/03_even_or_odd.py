def even_odd(*args):
    if args[-1] == "even":
        even_odd_list = [num for num in args[:-1] if num % 2 == 0]
    elif args[-1] == "odd":
        even_odd_list = [num for num in args[:-1] if num % 2 != 0]
    return even_odd_list


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
