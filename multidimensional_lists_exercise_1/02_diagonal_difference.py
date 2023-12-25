# matrix = [[int(x) for x in input().split()]for _ in range(int(input()))]

# sum_primary_diagonal = 0
# sum_secondary_diagonal = 0

# # for row in range(len(matrix)):
# #   sum_primary_diagonal += matrix[row][row] OR
# sum_primary_diagonal = sum([matrix[row][row]for row in range(len(matrix))])

# # for row in range(len(matrix)):
# #   sum_secondary_diagonal += matrix[row][len(matrix) - 1 - row] OR
# sum_secondary_diagonal = sum([matrix[row][len(matrix) - 1 - row] for row in range(len(matrix))])

# print(abs(sum_primary_diagonal - sum_secondary_diagonal))


#  OPTION 2

matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for row in range(len(matrix)):
    sum_primary_diagonal += matrix[row][row]
    sum_secondary_diagonal += matrix[row][len(matrix) - 1 - row]

print(abs(sum_primary_diagonal - sum_secondary_diagonal))
