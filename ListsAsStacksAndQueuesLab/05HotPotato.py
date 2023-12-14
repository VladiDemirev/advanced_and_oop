from collections import deque


# def hot_potato(kids_names, toss_number):
#   queue = deque(kids_names)
#   counter = 1
#   while len(queue) > 1:
#     if counter < toss_number:
#       queue.append(queue.popleft())
#       counter += 1
#     elif counter == toss_number:
#       print(f"Removed {queue.popleft()}")
#       counter = 1
#   return f"Last is {queue.popleft()}"


# names = input().split()
# toss = int(input())
# print(hot_potato(names, toss))


# OPTION 2

def hot_potato(kids_names, toss_number):
    queue = deque(kids_names)
    while len(queue) > 1:
        queue.rotate(-toss_number + 1)
        print(f"Removed {queue.popleft()}")
    return f"Last is {queue.popleft()}"


names = input().split()
toss = int(input())
print(hot_potato(names, toss))
