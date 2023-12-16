from collections import deque


def reverse_sring(input):
  reversed_stack = []
  while input:
    reversed_stack.append(input.pop())
  return ' '.join(reversed_stack)


input_string = input().split()
print(reverse_sring(input_string))


# OPTION 2

# def reverse_sring(input):
#     for _ in range(len(input)):
#         print(input.pop(), end=" ")
#
#
# input_string = deque(input().split())
# reverse_sring(input_string)
