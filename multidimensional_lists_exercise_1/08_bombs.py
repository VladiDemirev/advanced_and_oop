size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]


# for _ in range(size):
#     row = [int(x) for x in input().split()]
#     matrix.append(row)

bombs = input().split()

surrounding_cells = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
    "left_up": [-1, -1],
    "left_down": [1, -1],
    "right_up": [-1, 1],
    "right_down": [1, 1]
}


for bomb in bombs:
    row, col = bomb.split(",")
    bomb_row = int(row)
    bomb_col = int(col)
    if matrix[bomb_row][bomb_col] <= 0:
        continue
    for direction, coordinates in surrounding_cells.items():
        row = bomb_row + coordinates[0]
        col = bomb_col + coordinates[1]
        if row not in range(size) or col not in range(size):
            continue
        if matrix[row][col] <= 0:
            continue
        matrix[row][col] -= matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0

alive_cells = [num for row in matrix for num in row if num > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
