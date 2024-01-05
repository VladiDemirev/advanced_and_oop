rows = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(rows)]
command = input()

while command != "END":
    operation, *args = command.split()
    row = int(args[0])
    col = int(args[1])
    value = int(args[2])
    if row not in range(rows) or col not in range(rows):
        print("Invalid coordinates")
    else:
        if operation == "Add":
            matrix[row][col] += value
        elif operation == "Subtract":
            matrix[row][col] -= value
    command = input()

[print(*row) for row in matrix]
