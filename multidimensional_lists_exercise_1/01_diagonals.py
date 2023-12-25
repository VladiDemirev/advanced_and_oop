row_col = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(row_col)]

primary_diagonal = [matrix[row][row] for row in range(row_col)]
secondary_diagonal = [matrix[row][row_col - row - 1] for row in range(row_col)]

# row = 0
# for col in range(row_col - 1, -1, -1):
#   secondary_diagonal.append(matrix[row][col])
#   row += 1

print(f"Primary diagonal: {', '.join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}")
