# rows, cols = [int(x) for x in input().split(", ")]
# matrix = []
# sum_elements = 0

# for _ in range(rows):
#   inner_list = [int(x) for x in input().split(", ")]
#   matrix.append(inner_list)

# # for row in range(rows):
# #   for col in range(cols):
# #     sum_elements += matrix[row][col] OR
# for row in range(rows):
#   for col in range(len(matrix[row])):
#     sum_elements += matrix[row][col]

# print(sum_elements)
# print(matrix)


# OPTION 2

# rows, cols = [int(x) for x in input().split(", ")]
# matrix = []
# sum_elements = 0

# for _ in range(rows):
#   inner_list = [int(x) for x in input().split(", ")]
#   matrix.append(inner_list)
#   sum_elements += sum(inner_list)

# print(sum_elements)
# print(matrix)


#  OPTION 3

def create_matrix(row_index, col_index):
    matrix = []
    sum_elements = 0
    for _ in range(row_index):
        inner_list = [int(x) for x in input().split(", ")]
        matrix.append(inner_list)
        sum_elements += sum(inner_list)
    return f"{sum_elements}\n{matrix}"


rows, cols = [int(x) for x in input().split(", ")]

print(create_matrix(rows, cols))
