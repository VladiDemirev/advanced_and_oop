# rows, cols = [int(x) for x in input().split()]
# matrix = []
#
# for row in range(rows):
#     palindromes_row = []
#     for col in range(cols):
#         first_letter = last_letter = chr(97 + row)
#         middle_letter = chr(97 + row + col)
#         palindromes_row.append(first_letter + middle_letter + last_letter)
#     matrix.append(palindromes_row)
#
# [print(*row) for row in matrix]


# OPTION 2

rows, cols = [int(x) for x in input().split()]

start = ord("a")

for row in range(rows):
    for col in range(cols):
        print(f"{chr(start + row)}{chr(start + row + col)}{chr(start + row)}", end=" ")
    print()
