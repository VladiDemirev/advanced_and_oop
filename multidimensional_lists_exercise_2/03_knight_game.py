rows = int(input())
# matrix = [[x for x in input()] for _ in range(rows)]
matrix = []
knight_position = []
removed_knights = 0
moves = [(2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]

for row in range(rows):
    matrix.append([x for x in input()])
    for col in range(rows):
        if matrix[row][col] == "K":
            knight_position.append([row, col])

while True:
    max_hits = 0
    max_knight = [0, 0]
    for k_row, k_col in knight_position:
        current_hits = 0
        for move in moves:
            new_row = k_row + move[0]
            new_col = k_col + move[1]
            if new_row in range(rows) and new_col in range(rows):
                if matrix[new_row][new_col] == "K":
                    current_hits += 1
        if current_hits > max_hits:
            max_hits = current_hits
            max_knight = [k_row, k_col]
    if max_hits == 0:
        break
    knight_position.remove(max_knight)
    matrix[max_knight[0]][max_knight[1]] = "0"
    removed_knights += 1

print(removed_knights)
