import time


def summation_pairs(integers_list, sum_):
    for i in range(len(integers_list) - 1):
        if integers_list[i] == "":
            continue
        for j in range(i + 1, len(integers_list)):
            if integers_list[j] == "":
                continue
            if integers_list[i] + integers_list[j] == sum_:
                print(f"{integers_list[i]} + {integers_list[j]} = {sum_}")
                integers_list[i] = ""
                integers_list[j] = ""
                break


start = time.time()

integers = [int(x) for x in input().split()]
target_number = int(input())
summation_pairs(integers, target_number)

end = time.time()
print(f"Time range: {end-start}")


# OPTION 2

# import time
#
#
# def summation_pairs(integers_list, sum_):
#     targets = set()
#     values_map = {}
#     for value in integers_list:
#         if value in targets:
#             targets.remove(value)
#             pair = values_map[value]
#             del values_map[value]
#             print(f"{pair} + {value} = {sum_}")
#         else:
#             resulting_number = sum_ - value
#             targets.add(resulting_number)
#             values_map[resulting_number] = value
#
#
# start = time.time()
#
# integers = [int(x) for x in input().split()]
# target_number = int(input())
# summation_pairs(integers, target_number)
#
# end = time.time()
# print(f"Time range: {end-start}")
