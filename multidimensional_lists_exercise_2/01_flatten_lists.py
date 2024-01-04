string = input().split("|")
matrix = []

for index in range(len(string) - 1, -1, -1):
    row = string[index].split()
    if row:
        matrix.append(row)

[print(*r, sep=" ", end=" ") for r in matrix]
