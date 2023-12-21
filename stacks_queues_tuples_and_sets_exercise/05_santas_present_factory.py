# from collections import deque
#
# materials = deque(int(x) for x in input().split())
# magic_level = deque(int(x) for x in input().split())
# presents = {
#     "Doll": 150,
#     "Wooden train": 250,
#     "Teddy bear": 300,
#     "Bicycle": 400,
# }
#
# Doll = 0
# Wooden_train = 0
# Teddy_bear = 0
# Bicycle = 0
#
# while materials and magic_level:
#     material = materials.pop()
#     magic = magic_level.popleft()
#     result = material * magic
#
#     if result < 0:
#         materials.append(material + magic)
#     elif result > 0 and result not in presents.values():
#         materials.append(material + 15)
#     elif result == 0:
#         if material == 0 and magic != 0:
#             magic_level.appendleft(magic)
#             continue
#         elif material != 0 and magic == 0:
#             materials.append(material)
#             continue
#         else:
#             continue
#     elif result == 150:
#         Doll += 1
#     elif result == 250:
#         Wooden_train += 1
#     elif result == 300:
#         Teddy_bear += 1
#     elif result == 400:
#         Bicycle += 1
#
# if (
#         (Doll > 0 and Wooden_train > 0) or
#         (Teddy_bear > 0 and Bicycle > 0)
# ):
#     print("The presents are crafted! Merry Christmas!")
# else:
#     print("No presents this Christmas!")
#
# if materials:
#     print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
# if magic_level:
#     print(f"Magic left: {', '.join(str(x) for x in magic_level)}")
#
# if Bicycle > 0:
#     print(f"Bicycle: {Bicycle}")
# if Doll > 0:
#     print(f"Doll: {Doll}")
# if Teddy_bear > 0:
#     print(f"Teddy bear: {Teddy_bear}")
# if Wooden_train > 0:
#     print(f"Wooden train: {Wooden_train}")


# OPTION 2

from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())
# print("True" if magic_levels[0] else "False")
# print()
crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0
    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product> 0:
        materials.append(material + 15)

if (
        {"Doll", "Wooden train"}.issubset(crafted) or
        {"Teddy bear", "Bicycle"}.issubset(crafted)
):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in reversed(materials))}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
