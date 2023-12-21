from collections import deque

chocolates = deque(int(x) for x in input().split(", "))
cups_milk = deque(int(x) for x in input().split(", "))

milkshakes = 0

while chocolates and cups_milk and milkshakes != 5:
    ingr_one = chocolates[-1]
    ingr_two = cups_milk[0]
    if ingr_one <= 0 and ingr_two <= 0:
        chocolates.pop()
        cups_milk.popleft()
        continue
    elif ingr_one <= 0:
        chocolates.pop()
        continue
    elif ingr_two <= 0:
        cups_milk.popleft()
        continue
    if ingr_one == ingr_two:
        milkshakes += 1
        chocolates.pop()
        cups_milk.popleft()
    else:
        cups_milk.append(cups_milk.popleft())
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join(str(x) for x in chocolates)}")
else:
    print("Chocolate: empty")

if cups_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_milk)}")
else:
    print("Milk: empty")

# from collections import deque
#
# chocolates = deque(int(x) for x in input().split(", "))
# cups_milk = deque(int(x) for x in input().split(", "))
#
# milkshakes = 0
#
# while chocolates and cups_milk and milkshakes != 5:
#     ingr_one = chocolates.pop()
#     ingr_two = cups_milk.popleft()
#     if ingr_one <= 0 and ingr_two <= 0:
#         continue
#     elif ingr_one <= 0:
#         cups_milk.appendleft(ingr_two)
#         continue
#     elif ingr_two <= 0:
#         chocolates.append(ingr_one)
#         continue
#     if ingr_one == ingr_two:
#         milkshakes += 1
#     else:
#         cups_milk.append(ingr_two)
#         chocolates.append(ingr_one - 5)
#
# if milkshakes == 5:
#     print("Great! You made all the chocolate milkshakes needed!")
# else:
#     print("Not enough milkshakes.")
#
# print(f"Chocolate: {(', '.join(str(x) for x in chocolates)) or 'empty'}")
# print(f"Milk: {(', '.join(str(x) for x in cups_milk)) or 'empty'}")
