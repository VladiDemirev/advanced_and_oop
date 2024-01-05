rows = int(input())
matrix = []
bunny = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "B":
            bunny = [row, col]

moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
max_eggs_matrix = []
max_eggs = float("-inf")
max_direction = ""

for direction, move in moves.items():
    collected_eggs = 0
    current_egg_matrix = []
    new_row = bunny[0] + move[0]
    new_col = bunny[1] + move[1]
    while new_row in range(rows) and new_col in range(rows):
        if matrix[new_row][new_col] == "X":
            break
        collected_eggs += int(matrix[new_row][new_col])
        current_egg_matrix.append([new_row, new_col])
        new_row += move[0]
        new_col += move[1]
    if collected_eggs > max_eggs and current_egg_matrix:
        max_eggs = collected_eggs
        max_eggs_matrix = current_egg_matrix
        max_direction = direction

print(max_direction)
# for row in max_eggs_matrix:
#     print(row)
[print(row) for row in max_eggs_matrix]
print(max_eggs)
