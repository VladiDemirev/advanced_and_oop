# from collections import deque
#
#
# def number_racks(stack, capacity):
#     sum_clothing = 0
#     count_racks = 0
#     while stack:
#         sum_clothing += stack[-1]
#         if sum_clothing == capacity:
#             count_racks += 1
#             sum_clothing = 0
#         elif sum_clothing > capacity:
#             sum_clothing = sum_clothing - (sum_clothing - stack[-1])
#             count_racks += 1
#         stack.pop()
#     if sum_clothing > 0:
#         count_racks += 1
#     return count_racks
#
#
# clothes_stack = deque([int(x) for x in input().split()])
# rack_capacity = int(input())
#
# print(number_racks(clothes_stack, rack_capacity))


# OPTION 2

from collections import deque


def number_racks(stack, capacity):
    current_rack_space = capacity
    count_racks = 1
    while stack:
        cloth = stack.pop()
        if cloth <= current_rack_space:
            current_rack_space -= cloth
        else:
            count_racks += 1
            current_rack_space = capacity - cloth
    return count_racks


clothes_stack = deque([int(x) for x in input().split()])
rack_capacity = int(input())

print(number_racks(clothes_stack, rack_capacity))
