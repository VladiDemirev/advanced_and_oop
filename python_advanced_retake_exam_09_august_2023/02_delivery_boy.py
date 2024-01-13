rows, cols = [int(x) for x in input().split()]

matrix = []
delivery_boy_pos = []
delivery_address_pos = []
restaurant_pos = []

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(cols):
        if matrix[row][col] == "B":
            delivery_boy_pos = [row, col]
        elif matrix[row][col] == "A":
            delivery_address_pos = [row, col]
        elif matrix[row][col] == "P":
            restaurant_pos = [row, col]

moves = {"up": [-1, 0], "down": [1, 0], "right": [0, 1], "left": [0, -1]}
delivery_boy_new_pos = delivery_boy_pos

while True:
    direction = input()
    row = delivery_boy_new_pos[0] + moves[direction][0]
    col = delivery_boy_new_pos[1] + moves[direction][1]
    if row in range(rows) and col in range(cols):
        if matrix[row][col] == "P":
            print("Pizza is collected. 10 minutes for delivery.")
            matrix[row][col] = "R"
        elif matrix[row][col] == "A":
            print("Pizza is delivered on time! Next order...")
            matrix[row][col] = "P"
            break
        elif matrix[row][col] == "*":
            continue
        elif matrix[row][col] == "-":
            matrix[row][col] = "."
        delivery_boy_new_pos = [row, col]
    else:
        print("The delivery is late. Order is canceled.")
        matrix[delivery_boy_pos[0]][delivery_boy_pos[1]] = " "
        break

# print(matrix)
[print(''.join(row)) for row in matrix]


