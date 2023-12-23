# def sum_matrix_columns(rows_index, cols_index):
#   matrix = [[int(x) for x in input().split()] for _ in range(rows_index)]
#   for col in range(cols_index):
#     sum_col = 0
#     for row in range(rows_index):
#       sum_col += matrix[row][col]
#     print(sum_col)


# rows, cols = [int(x) for x in input().split(", ")]
# sum_matrix_columns(rows, cols)


#  OPTION 2

def sum_matrix_columns(rows_index, cols_index):
    matrix = [[int(x) for x in input().split()] for _ in range(rows_index)]
    sum_list = []
    for col in range(cols_index):
        sum_col = 0
        for row in range(rows_index):
            sum_col += matrix[row][col]
        sum_list.append(sum_col)
    return sum_list


rows, cols = [int(x) for x in input().split(", ")]
print(*sum_matrix_columns(rows, cols), sep="\n")
