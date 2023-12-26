rows, cols = [int(x) for x in input().split()]
equal_cells_count = 0

matrix = [[x for x in input().split()] for row in range(rows)]

for row in range(rows - 1):
    for col in range(cols - 1):
        current_el = matrix[row][col]
        next_el = matrix[row][col + 1]
        lower_el = matrix[row + 1][col]
        diagonal_el = matrix[row + 1][col + 1]
        if current_el == next_el == lower_el == diagonal_el:
            equal_cells_count += 1
        # else:
        #     continue

print(equal_cells_count)
