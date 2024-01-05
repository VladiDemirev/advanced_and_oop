presents = int(input())
rows = int(input())

matrix = []
santa_position = []

nice_kids = []
presents_given = 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "S":
            santa_position = [row, col]

        elif matrix[row][col] == "V":
            nice_kids.append([row, col])

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

while presents > 0:
    command = input()
    if command == "Christmas morning":
        break
    matrix[santa_position[0]][santa_position[1]] = "-"
    row = santa_position[0] + moves[command][0]
    col = santa_position[1] + moves[command][1]
    santa_position = [row, col]
    if matrix[row][col] == "V":
        presents -= 1
        presents_given += 1
        matrix[row][col] = "S"
        if presents == 0:
            break
    elif matrix[row][col] == "X":
        matrix[row][col] = "S"
    elif matrix[row][col] == "C":
        matrix[row][col] = "S"
        for x, y in moves.values():
            r = santa_position[0] + x
            c = santa_position[1] + y
            if matrix[r][c] in "X, V":
                if matrix[r][c] == "V":
                    presents_given += 1
                presents -= 1
                matrix[r][c] = "-"

            if presents == 0:
                break

if not presents and presents_given < len(nice_kids):
    print("Santa ran out of presents!")

[print(*row) for row in matrix]

if presents_given == len(nice_kids):
    print(f"Good job, Santa! {presents_given} happy nice kid/s.")
else:
    print(f"No presents for {len(nice_kids) - presents_given} nice kid/s.")




# ======66/100==============================

# presents = int(input())
# rows = int(input())
#
# matrix = []
# santa_position = []
# nice_kids = []
# presents_given = 0
#
# for row in range(rows):
#     matrix.append([x for x in input().split()])
#     for col in range(rows):
#         if matrix[row][col] == "S":
#             santa_position = [row, col]
#         elif matrix[row][col] == "V":
#             nice_kids.append([row, col])
#
# moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
#
# while presents > 0:
#     command = input()
#     if command == "Christmas morning":
#         break
#     matrix[santa_position[0]][santa_position[1]] = "-"
#     row = santa_position[0] + moves[command][0]
#     col = santa_position[1] + moves[command][1]
#     santa_position = [row, col]
#     if matrix[row][col] == "V":
#         presents -= 1
#         presents_given += 1
#         matrix[row][col] = "S"
#         if presents == 0:
#             break
#     elif matrix[row][col] == "X":
#         matrix[row][col] = "S"
#     if matrix[row][col] == "C":
#         matrix[row][col] = "S"
#         santa_position = [row, col]
#         surrounding_cells = [(santa_position[0] - 1, santa_position[1]),
#                              (santa_position[0] + 1, santa_position[1]),
#                              (santa_position[0], santa_position[1] - 1),
#                              (santa_position[0], santa_position[1] + 1)
#                              ]
#         for cell in surrounding_cells:
#             if matrix[cell[0]][cell[1]] in "X, V":
#                 presents -= 1
#                 if presents == 0:
#                     break
#                 if matrix[cell[0]][cell[1]] == "V":
#                     presents_given += 1
#                 # if presents == 0:
#                 #     break
#                 matrix[cell[0]][cell[1]] = "-"
#     # santa_position = [row, col]
#
# if presents == 0:
#     print("Santa ran out of presents!")
# [print(*row) for row in matrix]
# if presents_given == len(nice_kids):
#     print(f"Good job, Santa! {presents_given} happy nice kid/s.")
# else:
#     print(f"No presents for {len(nice_kids) - presents_given} nice kid/s.")

#===============================================


# presents = int(input())
# rows = int(input())
#
# matrix = []
# santa_position = []
#
# total_nice_kids = 0
# nice_kids_visited = 0
#
# for row in range(rows):
#     matrix.append([x for x in input().split()])
#     for col in range(rows):
#         if matrix[row][col] == "S":
#             santa_position = [row, col]
#             matrix[santa_position[0]][santa_position[1]] = "-"
#
#         elif matrix[row][col] == "V":
#             total_nice_kids += 1
#
# moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
#
# while presents > 0:
#     command = input()
#     if command == "Christmas morning":
#         break
#     row = santa_position[0] + moves[command][0]
#     col = santa_position[1] + moves[command][1]
#     santa_position = [row, col]
#     if matrix[row][col] == "V":
#         presents -= 1
#         nice_kids_visited += 1
#         if presents == 0:
#             break
#     elif matrix[row][col] == "C":
#         for x, y in moves.values():
#             r = santa_position[0] + x
#             c = santa_position[1] + y
#             if matrix[r][c] in "X, V":
#                 if matrix[r][c] == "V":
#                     nice_kids_visited += 1
#                 presents -= 1
#                 matrix[r][c] = "-"
#             if presents == 0:
#                 break
#     matrix[santa_position[0]][santa_position[1]] = "-"
#     if not presents or total_nice_kids == nice_kids_visited:
#         break
#
# matrix[santa_position[0]][santa_position[1]] = "S"
#
# if not presents and nice_kids_visited < total_nice_kids:
#     print("Santa ran out of presents!")
#
# [print(*row) for row in matrix]
#
# if nice_kids_visited == total_nice_kids:
#     print(f"Good job, Santa! {total_nice_kids} happy nice kid/s.")
# else:
#     print(f"No presents for {total_nice_kids - nice_kids_visited} nice kid/s.")










