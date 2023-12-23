# def flattened_matrix(rows_index):
#   matrix = [input().split(", ") for row in range(rows_index)]
#   # flattened = [[list_el in matrix] for el in list_el]
#   flattened = []
#   for row in range(rows_index):
#     for col in range(len(matrix[row])):
#       flattened.append(int(matrix[row][col]))
#   return flattened


# rows = int(input())
# print(flattened_matrix(rows))


# OPTION 2

# def flattened_matrix(rows_index):
#   matrix = [input().split(", ") for row in range(rows_index)]
#   flattened = [int(el) for row in matrix for el in row]
#   return flattened


# rows = int(input())
# print(flattened_matrix(rows))


# OPTION 3

def flattened_matrix(rows_index):
    flattened = []
    for _ in range(rows_index):
        el_list = [int(el) for el in input().split(", ")]
        flattened.extend(el_list)
    return flattened


rows = int(input())
print(flattened_matrix(rows))
