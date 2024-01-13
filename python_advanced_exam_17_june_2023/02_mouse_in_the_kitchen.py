rows, cols = [int(x) for x in input().split(",")]

matrix = []
mouse_pos = []
mouse_new_pos = []
cheese_count = 0

for row in range(rows):
    matrix.append(list(input()))
    for col in range(cols):
        if matrix[row][col] == "M":
            mouse_pos = [row, col]
            mouse_new_pos = mouse_pos
            # matrix[row][col] = "*"
        if matrix[row][col] == "C":
            cheese_count += 1

moves = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

while True:
    command = input()
    if command == "danger":
        if cheese_count > 0:
            print("Mouse will come back later!")
        break

    row = mouse_new_pos[0] + moves[command][0]
    col = mouse_new_pos[1] + moves[command][1]

    if row not in range(rows) or col not in range(cols):
        print("No more cheese for tonight!")
        matrix[mouse_new_pos[0]][mouse_new_pos[1]] = "M"
        break

    if matrix[row][col] == "C":
        cheese_count -= 1
        if cheese_count == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            mouse_new_pos = [row, col]
            matrix[row][col] = "M"
            break
        matrix[row][col] = "*"

    elif matrix[row][col] == "T":
        print("Mouse is trapped!")
        mouse_new_pos = [row, col]
        matrix[row][col] = "M"
        break

    elif matrix[row][col] == "@":
        continue

    mouse_new_pos = [row, col]

if mouse_pos != mouse_new_pos:
    matrix[mouse_pos[0]][mouse_pos[1]] = "*"

[print(''.join(row)) for row in matrix]
# for row in matrix:
#   print(''.join(row))
