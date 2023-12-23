def is_symbol(matrix_size):
    # matrix = [[char for char in input()] for _ in range(matrix_size)] OR
    matrix = [list(input()) for _ in range(matrix_size)]
    searched_symbol = input()
    for row in range(matrix_size):
        for col in range(matrix_size):
            if matrix[row][col] == searched_symbol:
                return f"({row}, {col})"
    return f"{searched_symbol} does not occur in the matrix"


size = int(input())
print(is_symbol(size))
