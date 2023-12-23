# def even_matrix(rows_index):
#   matrix = []
#   for _ in range(rows_index):
#     matrix.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])
#   return matrix


# rows = int(input())
# print(even_matrix(rows))


# OPTION 2

def even_matrix(rows_index):
    matrix = [[int(x) for x in input().split(", ") if int(x) % 2 == 0] for row in range(rows_index)]
    return matrix


rows = int(input())
print(even_matrix(rows))
