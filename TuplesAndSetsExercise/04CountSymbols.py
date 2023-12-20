def count_symbols(text):
    sorted_text_set = sorted(set(text))
    # for el in sorted(set(text)):
    for el in sorted_text_set:
        print(f"{el}: {text.count(el)} time/s")


text_input = input()
count_symbols(text_input)

# OPTION 2

# def count_symbols(text):
#   occurances = {}
#   for el in sorted(text):
#     if el not in occurances:
#       occurances[el] = 0
#     occurances[el] += 1
#   for char, occ in occurances.items():
#     print(f"{char}: {occ} time/s")


# text_input = input()
# count_symbols(text_input)


# OPTION 3

# from collections import defaultdict


# def count_symbols(text):
#   occurances = defaultdict(lambda: 0)
#   for el in sorted(text):
#     occurances[el] += 1
#   for char, occ in occurances.items():
#     print(f"{char}: {occ} time/s")


# text_input = input()
# count_symbols(text_input)


# OPTION 4

# def count_symbols(text):
#   occurances = {}
#   for el in sorted(text):
#     occurances[el] = occurances.get(el, 0) + 1
#   for char, occ in occurances.items():
#     print(f"{char}: {occ} time/s")


# text_input = input()
# count_symbols(text_input)
