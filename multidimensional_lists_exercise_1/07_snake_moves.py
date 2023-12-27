#   OPTION 1

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]
#
# matrix = [["" for _ in range(cols)] for _ in range(rows)]
# snake = deque(input())
# snake_copy = snake.copy()
#
# for row in range(rows):
#     if row % 2 == 0:
#         for col in range(cols):
#             if not snake_copy:
#                 snake_copy = snake.copy()
#             matrix[row][col] = snake_copy.popleft()
#
#     else:
#         for col in range(cols - 1, -1, -1):
#             if not snake_copy:
#                 snake_copy = snake.copy()
#             matrix[row][col] = snake_copy.popleft()
#
# for row in range(len(matrix)):
#     print("".join(matrix[row]))


#   OPTION 2

from collections import deque

rows, cols = [int(x) for x in input().split()]

matrix = [["" for _ in range(cols)] for _ in range(rows)]
snake = deque(input())
snake_copy = snake.copy()

for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            if not snake_copy:
                snake_copy = snake.copy()
            matrix[row][col] = snake_copy.popleft()

    else:
        for col in range(cols - 1, -1, -1):
            if not snake_copy:
                snake_copy = snake.copy()
            matrix[row][col] = snake_copy.popleft()

for row in range(len(matrix)):
    print("".join(matrix[row]))
