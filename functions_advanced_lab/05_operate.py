# from functools import reduce


# def operate(sign, *args):
#   if sign == "+":
#     result = reduce(lambda a, b: a + b, args)
#   elif sign == "-":
#     result = reduce(lambda a, b: a - b, args)
#   elif sign == "*":
#     result = reduce(lambda a, b: a * b, args)
#   elif sign == "/":
#     result = reduce(lambda a, b: a / b, args)

#   return result


# def operate(sign, *args):
#   if sign == "+":
#     result = 0
#     for arg in args:
#       result += arg
#   elif sign == "-":
#     result = args[0]
#     for arg in args[1:]:
#       result -= arg
#   elif sign == "*":
#     result = 1
#     for arg in args:
#       result *= arg
#   elif sign == "/":
#     result = args[0]
#     for arg in args[1:]:
#       result /= arg

#   return result

# print(operate("-", 1, 2, 3))
# print(operate("/", 0, 4))


from functools import reduce


def operate(sign, *args):
    result = reduce(lambda a, b: eval(f"{str(a)}{sign}{str(b)}"), args)

    return result


print(operate("-", 1, 2, 3))
print(operate("/", 0, 4))
