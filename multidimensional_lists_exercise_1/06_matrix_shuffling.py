#   OPTION 1

rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    line = input()
    if line == "END":
        break
    command = line.split()
    if command[0] != "swap" or len(command) != 5:
        print("Invalid input!")
        continue

    row_1, col_1, row_2, col_2 = [int(x) for x in command[1:]]

    if (
            ((row_1 or row_2) not in range(rows)) or
            ((col_1 or col_2) not in range(cols))
    ):
        print("Invalid input!")
    else:
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        [print(*row) for row in matrix]


#   OPTION 2

# rows, cols = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# command = input()
# while command != "END":
#     command = command.split()
#     if command[0] == "swap" and len(command) == 5:
#         # NO NEED FOR BELOW CHECK AS NO SUCH TEST IN JUDGE
#         for i in command[1:]:
#             if not i.isdigit():
#                 print("Invalid input!")
#                 break
#         else:
#             row_1 = int(command[1])
#             col_1 = int(command[2])
#             row_2 = int(command[3])
#             col_2 = int(command[4])
#             if (
#                     ((row_1 and row_2) in range(rows)) and
#                     ((col_1 and col_2) in range(cols))
#             ):
#                 matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
#                 [print(*row) for row in matrix]
#             else:
#                 print("Invalid input!")
#     else:
#         print("Invalid input!")
#     command = input()
