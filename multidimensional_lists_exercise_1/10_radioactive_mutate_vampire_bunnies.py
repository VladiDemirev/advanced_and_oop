rows, cols = [int(x) for x in input().split()]
matrix = []
player_pos = []
bunnies = []
is_won = False
is_dead = False
is_won_pos = []
is_dead_pos = []

for idx in range(rows):
    row = list(input())
    matrix.append(row)
    for el in row:
        if el == "P":
            player_pos = [idx, row.index("P")]
        if el == "B":
            bunnies.append((idx, row.index("B")))

moves = list(input())

directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}


def update_bunnies():
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B" and (row, col) not in bunnies:
                bunnies.append((row, col))
    return bunnies


def spread_bunnies():
    for b in update_bunnies():
        for d in directions:
            new_bunny_row = b[0] + directions[d][0]
            new_bunny_col = b[1] + directions[d][1]
            if (new_bunny_row in range(rows) and new_bunny_col in range(cols)) and matrix[new_bunny_row][
                new_bunny_col] != "B":
                matrix[new_bunny_row][new_bunny_col] = "B"
    return matrix


for move in moves:
    matrix[player_pos[0]][player_pos[1]] = "."
    spread_bunnies()
    current_row = player_pos[0] + directions[move][0]
    current_col = player_pos[1] + directions[move][1]
    if current_row not in range(rows) or current_col not in range(cols):
        is_won = True
        is_won_pos = player_pos
        break
    elif matrix[current_row][current_col] == "B":
        is_dead = True
        is_dead_pos = [current_row, current_col]
        break
    player_pos = [current_row, current_col]
    matrix[current_row][current_col] = "P"
    update_bunnies()

[print(*row, sep="") for row in matrix]
if is_won:
    print(f"won: {' '.join(str(x) for x in is_won_pos)}")
elif is_dead:
    print(f"dead: {' '.join(str(x) for x in is_dead_pos)}")
