def push(number, stack):
    stack.append(number)
    return stack


def delete(stack):
    if stack:
        stack.pop()
    return stack


def queries(lines):
    stack = []
    max_el = 0
    min_el = 0
    for _ in range(lines):
        command = input().split()
        query = command[0]
        if query == "1":
            number = command[1]
            stack = push(number, stack)
            # if len(stack) == 1:
            #     max_el = int(number)
            #     min_el = int(number)
            # else:
            #     if int(number) > int(max_el):
            #         max_el = number
            #     if int(number) < int(min_el):
            #         min_el = number
        elif query == "2":
            stack = delete(stack)
        elif query == "3" and stack:
            print(max(stack))
            # print(max_el)
        elif query == "4" and stack:
            print(min(stack))
            # print(min_el)
    stack.reverse()
    return ", ".join(stack)


num_lines = int(input())
print(queries(num_lines))


# OPTION 2

# from collections import deque
#
# num_lines = int(input())
# queue = deque()
#
# map_functions = {
#     1: lambda x: x.append(command[1]),
#     2: lambda x: x.pop() if x else None,
#     3: lambda x: print(max(x)) if x else None,
#     4: lambda x: print(min(x)) if x else None
# }
#
# for _ in range(num_lines):
#     command = [int(x) for x in input().split()]
#     map_functions[command[0]](queue)
#
# queue.reverse()
#
# print(*queue, sep=", ")
