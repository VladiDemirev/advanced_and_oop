rows = 5
matrix = []
shooter = []
total_targets = 0

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            shooter = [row, col]
        elif matrix[row][col] == "x":
            total_targets += 1

shot_targets_positions = []
moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

commands_count = int(input())

for _ in range(commands_count):
    command, *args = input().split()
    direction = args[0]
    if command == "move":
        steps = int(args[1])
        new_row = shooter[0] + (moves[direction][0] * steps)
        new_col = shooter[1] + (moves[direction][1] * steps)
        if new_row in range(rows) and new_col in range(rows) and matrix[new_row][new_col] == ".":
            shooter = [new_row, new_col]
    elif command == "shoot":
        new_row = shooter[0] + moves[direction][0]
        new_col = shooter[1] + moves[direction][1]
        while new_row in range(rows) and new_col in range(rows):
            if matrix[new_row][new_col] == "x":
                total_targets -= 1
                matrix[new_row][new_col] = "."
                shot_targets_positions.append([new_row, new_col])
                break
            new_row += moves[direction][0]
            new_col += moves[direction][1]
        if total_targets == 0:
            print(f"Training completed! All {len(shot_targets_positions)} targets hit.")
            break

if total_targets > 0:
    print(f"Training not completed! {total_targets} targets left.")
if shot_targets_positions:
    [print(row) for row in shot_targets_positions]





