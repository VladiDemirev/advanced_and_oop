from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = list(map(int, input().split()))
wasted_water = 0

while cups and bottles:
    bottle = bottles.pop()
    cup = cups[0]
    if cup > bottle:
        cups[0] -= bottle
        continue
    cups.popleft()
    bottle -= cup
    wasted_water += bottle

if not cups:
    print(f"Bottles: {' '.join(str(b) for b in bottles)}")
if not bottles:
    print(f"Cups: {' '.join(str(c) for c in cups)}")
print(f"Wasted litters of water: {wasted_water}")
