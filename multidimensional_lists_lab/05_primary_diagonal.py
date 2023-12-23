def sum_primary_diagonal(matrix_size):
    matrix = [[int(x) for x in input().split()] for _ in range(matrix_size)]
    diagonal = 0
    for row in range(matrix_size):
        diagonal += matrix[row][row]
    return diagonal


size = int(input())
print(sum_primary_diagonal(size))
