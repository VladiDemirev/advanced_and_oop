size = int(input())
matrix = []
ship_pos = []

QUOTA = 20
collected_fish = 0

for row in range(size):
    current_row = list(input())
    if "S" in current_row:
        ship_pos = [row, current_row.index("S")]
        current_row[current_row.index("S")] = "-"
    matrix.append(current_row)

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

while True:
    command = input()

    if command == "collect the nets":
        matrix[ship_pos[0]][ship_pos[1]] = "S"
        break

    row = ship_pos[0] + moves[command][0]
    col = ship_pos[1] + moves[command][1]

    # if row not in range(size):
    #     row = 0
    # if col not in range(size):
    #     col = 0

    if row < 0:
        row = size - 1
    if row > size - 1:
        row = 0
    if col < 0:
        col = size - 1
    if col > size - 1:
        col = 0

    if matrix[row][col].isdigit():
        collected_fish += int(matrix[row][col])
        matrix[row][col] = "-"
    if matrix[row][col] == "W":
        ship_pos = [row, col]
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{ship_pos[0]},{ship_pos[1]}]")
        exit()

    ship_pos = [row, col]

if collected_fish >= QUOTA:
    print("Success! You managed to reach the quota!")
else:
    print(
        f"You didn't catch enough fish and didn't reach the quota! You need {QUOTA - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

[print(*row, sep="") for row in matrix]
