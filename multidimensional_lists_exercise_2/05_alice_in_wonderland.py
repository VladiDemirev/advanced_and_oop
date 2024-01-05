rows = int(input())
matrix = []
alice = []

for row in range(rows):
    matrix.append([x for x in input().split()])
    for col in range(rows):
        if matrix[row][col] == "A":
            alice = [row, col]

moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
tea_bags = 0

while tea_bags < 10:
    matrix[alice[0]][alice[1]] = "*"
    direction = input()
    alice[0] += moves[direction][0]
    alice[1] += moves[direction][1]
    if alice[0] not in range(rows) or alice[1] not in range(rows):
        break
    elif matrix[alice[0]][alice[1]] not in "R.*":
        tea_bags += int(matrix[alice[0]][alice[1]])
    elif matrix[alice[0]][alice[1]] == "R":
        matrix[alice[0]][alice[1]] = "*"
        break

if tea_bags >= 10:
    matrix[alice[0]][alice[1]] = "*"
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")
# [print(*row) for row in matrix]
[print(" ".join(row)) for row in matrix]
