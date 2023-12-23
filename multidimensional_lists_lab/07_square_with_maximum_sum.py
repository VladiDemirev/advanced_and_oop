def max_sum_square(rows_index, cols_index):
    matrix = [[int(x) for x in input().split(", ")] for _ in range(rows_index)]
    biggest_sum = float('-inf')
    submatrix = []
    for col in range(cols_index - 1):
        for row in range(rows_index - 1):
            top_left_el = matrix[row][col]
            top_right_el = matrix[row][col + 1]
            bottom_left_el = matrix[row + 1][col]
            bottom_right_el = matrix[row + 1][col + 1]
            sum_el = top_left_el + top_right_el + bottom_left_el + bottom_right_el
            if sum_el > biggest_sum:
                biggest_sum = sum_el
                submatrix = [[top_left_el, top_right_el], [bottom_left_el, bottom_right_el]]
    # return submatrix, biggest_sum
    for row in submatrix:
        print(" ".join(str(el) for el in row))
    print(biggest_sum)


rows, cols = [int(x) for x in input().split(", ")]
max_sum_square(rows, cols)
