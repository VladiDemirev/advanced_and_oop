# from collections import deque
#
# working_bees = deque(int(x) for x in input().split())
# nectar_deck = deque(int(x) for x in input().split())
# symbols = deque(input().split())
#
# total_honey = 0
#
# while working_bees and nectar_deck:
#     bee = working_bees.popleft()
#     nectar = nectar_deck.pop()
#     if nectar >= bee:
#         symbol = symbols.popleft()
#         if symbol == "/" and nectar == 0:
#             continue
#         total_honey += abs(eval(f"{bee} {symbol} {nectar}"))
#     else:
#         working_bees.appendleft(bee)
#         continue
#
# print(f"Total honey made: {total_honey}")
# if working_bees:
#     print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
# if nectar_deck:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar_deck)}")


# OPTION 2

# from collections import deque
#
# working_bees = deque(int(x) for x in input().split())
# nectar_deck = deque(int(x) for x in input().split())
# symbols = deque(input().split())
#
# total_honey = 0
#
# while working_bees and nectar_deck:
#     bee = working_bees.popleft()
#     nectar = nectar_deck.pop()
#     if nectar >= bee:
#         symbol = symbols.popleft()
#         if symbol == "*":
#             total_honey += abs(bee * nectar)
#         elif symbol == "/":
#             if nectar == 0:
#                 continue
#             else:
#                 total_honey += abs(bee / nectar)
#         elif symbol == "+":
#             total_honey += abs(bee + nectar)
#         elif symbol == "-":
#             total_honey += abs(bee - nectar)
#     else:
#         working_bees.appendleft(bee)
#         continue
#
# print(f"Total honey made: {total_honey}")
# if working_bees:
#     print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
# if nectar_deck:
#     print(f"Nectar left: {', '.join(str(x) for x in nectar_deck)}")


# OPTION 3

from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar_deck = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0

functions = {
    "*": lambda bees, nectars: bees * nectars,
    "/": lambda bees, nectars: bees / nectars,
    "+": lambda bees, nectars: bees + nectars,
    "-": lambda bees, nectars: bees - nectars,
}

while working_bees and nectar_deck:
    bee = working_bees.popleft()
    nectar = nectar_deck.pop()
    if nectar >= bee:
        symbol = symbols.popleft()
        if symbol == "/" and nectar == 0:
            continue
        total_honey += abs(functions[symbol](bee, nectar))
    else:
        working_bees.appendleft(bee)
        continue

print(f"Total honey made: {total_honey}")
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar_deck:
    print(f"Nectar left: {', '.join(str(x) for x in nectar_deck)}")
