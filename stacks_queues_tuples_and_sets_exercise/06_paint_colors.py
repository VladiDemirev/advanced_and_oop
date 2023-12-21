# from collections import deque
#
# color_string = deque(input().split())
# main_colors = []
#
# while color_string:
#     if len(color_string) == 1:
#         result = color_string.pop()
#         if result in ("red", "yellow", "blue", "orange", "purple", "green"):
#             main_colors.append(result)
#             continue
#         else:
#             continue
#     elif len(color_string) > 1:
#         sub_one = color_string.popleft()
#         sub_two = color_string.pop()
#         result_one = sub_one + sub_two
#         result_two = sub_two + sub_one
#         if result_one in ("red", "yellow", "blue", "orange", "purple", "green"):
#             main_colors.append(result_one)
#         elif result_two in ("red", "yellow", "blue", "orange", "purple", "green"):
#             main_colors.append(result_two)
#         else:
#             sub_one = sub_one[:-1]
#             sub_two = sub_two[:-1]
#             middle_deck = len(color_string) // 2
#             if sub_one and sub_two:
#                 color_string.insert(middle_deck, sub_one)
#                 color_string.insert(middle_deck + 1, sub_two)
#             elif not sub_one and sub_two:
#                 color_string.insert(middle_deck, sub_two)
#             elif not sub_two and sub_one:
#                 color_string.insert(middle_deck, sub_one)
#
# if "orange" in main_colors:
#     if "red" and "yellow" not in main_colors:
#         main_colors.remove("orange")
# if "purple" in main_colors:
#     if "red" and "blue" not in main_colors:
#         main_colors.remove("purple")
# if "green" in main_colors:
#     if "blue" and "yellow" not in main_colors:
#         main_colors.remove("green")
#
# print(main_colors)


#   OPTION 2

from collections import deque

color_string = deque(input().split())
colors = ["red", "yellow", "blue", "orange", "purple", "green"]
color_deck = []
req_colors = {
    "orange": {"red", "yellow"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

while color_string:
    substring_one = color_string.popleft()
    substring_two = color_string.pop() if color_string else ""

    for color in (substring_one + substring_two, substring_two + substring_one):
        if color in colors:
            color_deck.append(color)
            break
    else:
        for word in (substring_one[:-1], substring_two[:-1]):
            if word:
                color_string.insert(len(color_string) // 2, word)

for color in set(req_colors.keys()).intersection(color_deck):
    if not req_colors[color].issubset(color_deck):
        color_deck.remove(color)

print(color_deck)

