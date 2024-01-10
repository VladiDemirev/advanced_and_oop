# def func_executor(*args):
#   result = ""
#   for function in args:
#     func = function[0]
#     parameters = function[1]
#     result += f"{func.__name__} - {func(*parameters)}\n"
#   return result


#  OPTION 2

def func_executor(*args):
    result = []
    for func, data in args:
        result.append(f"{func.__name__} - {func(*data)}")
    return '\n'.join(result)


def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result


def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result


print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))
