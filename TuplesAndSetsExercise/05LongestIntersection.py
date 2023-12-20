# def longest_intersection(count_num):
#   longest_intersection = set()
#   for _ in range(count_num):
#     first, second = input().split("-")
#     first_start, first_end = first.split(",")
#     second_start, second_end = second.split(",")
#     first_set = {int(x) for x in range(int(first_start), int(first_end) + 1)}
#     second_set = {int(x) for x in range(int(second_start), int(second_end) + 1)}
#   # intersection = first_set.intersection(second_set) OR
#     intersection = first_set & second_set
#     if len(intersection) > len(longest_intersection):
#       longest_intersection = intersection
#   return f"Longest intersection is [{', '.join(str(x) for x in longest_intersection)}] \
# with length {len(longest_intersection)}"


# count = int(input())
# print(longest_intersection(count))


# OPTION 2

def longest_intersection(count_num):
    longest_intersection = set()
    for _ in range(count_num):
        first, second = [data.split(",") for data in input().split("-")]
        first_set = set(range(int(first[0]), int(first[1]) + 1))
        second_set = set(range(int(second[0]), int(second[1]) + 1))
        # intersection = first_set.intersection(second_set) OR
        intersection = first_set & second_set
        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection
    return (
        f"Longest intersection is "
        f"[{', '.join(str(x) for x in longest_intersection)}] "
        f"with length {len(longest_intersection)}"
    )


count = int(input())
print(longest_intersection(count))
