def periodic_table(lines):
    elements = set()
    for _ in range(lines):
        elements_to_add = set(input().split())
        # elements |= elements_to_add OR
        elements = elements.union(elements_to_add)
    return elements


lines_count = int(input())
print(*periodic_table(lines_count), sep="\n")

# OPTION 2

# def periodic_table(lines):
#   elements = set()
#   for _ in range(lines):
#     for el in input().split():
#       elements.add(el)
#   return elements


# lines_count = int(input())
# print(*periodic_table(lines_count), sep="\n")
