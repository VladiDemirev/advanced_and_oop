# from collections import deque
#
#
# def expression_evaluator(expression_input):
#     idx = 0
#     while idx < len(expression_input):
#         element = expression_input[idx]
#         if element == "*":
#             for _ in range(idx - 1):
#                 expression_input.appendleft(int(expression_input.popleft()) * int(expression_input.popleft()))
#         elif element == "/":
#             for _ in range(idx - 1):
#                 expression_input.appendleft(int(expression_input.popleft()) // int(expression_input.popleft()))
#         elif element == "+":
#             for _ in range(idx - 1):
#                 expression_input.appendleft(int(expression_input.popleft()) + int(expression_input.popleft()))
#         elif element == "-":
#             for _ in range(idx - 1):
#                 expression_input.appendleft(int(expression_input.popleft()) - int(expression_input.popleft()))
#         if element in "*/+-":
#             del expression_input[1]
#             idx = 0
#         idx += 1
#     return expression_input
#
#
# expression = deque(input().split())
# print(*expression_evaluator(expression))


# OPTION 2

from collections import deque
from math import floor


def expression_evaluator(expression_input):
    idx = 0
    while idx < len(expression_input):
        element = expression_input[idx]
        if element in "*/+-":
            for _ in range(idx - 1):
                expression_input.appendleft(eval(f"{int(expression_input.popleft())} "
                                                 f"{element} {int(expression_input.popleft())}"))
            del expression_input[1]
            idx = 1
        idx += 1
    return expression_input


expression = deque(input().split())
print(floor(*expression_evaluator(expression)))
