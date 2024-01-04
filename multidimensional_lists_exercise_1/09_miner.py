size = int(input())
commands = list(input().split())

matrix = []
miner_pos = []
total_coal = 0

for row in range(size):
    elements = input().split()
    matrix.append(elements)
    if "s" in elements:
        miner_pos = [row, elements.index("s")]
    if "c" in elements:
        total_coal += elements.count("c")

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1],
}

for c in commands:
    current_row = miner_pos[0] + directions[c][0]
    current_col = miner_pos[1] + directions[c][1]
    if current_row not in range(size) or current_col not in range(size):
        continue
    if matrix[current_row][current_col] == "c":
        matrix[current_row][current_col] = "*"
        total_coal -= 1
        if total_coal <= 0:
            print(f"You collected all coal! ({current_row}, {current_col})")
            break
    if matrix[current_row][current_col] == "e":
        print(f"Game over! ({current_row}, {current_col})")
        break
    miner_pos = [current_row, current_col]
else:
    print(f"{total_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
