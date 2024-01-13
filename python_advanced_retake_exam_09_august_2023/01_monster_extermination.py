from collections import deque

monsters_armour = deque([int(x) for x in input().split(",")])
soldier_stikes_strength = deque([int(x) for x in input().split(",")])

killed_monsters = 0

while monsters_armour and soldier_stikes_strength:
    monster = monsters_armour.popleft()
    soldier_strike = soldier_stikes_strength.pop()
    if soldier_strike >= monster:
        killed_monsters += 1
        if soldier_stikes_strength:
            soldier_stikes_strength[-1] += (soldier_strike - monster)
        elif (soldier_strike - monster) != 0:
            soldier_stikes_strength.append((soldier_strike - monster))
    else:
        monsters_armour.append(monster - soldier_strike)

if not monsters_armour:
    print("All monsters have been killed!")
if not soldier_stikes_strength:
    print("The soldier has been defeated.")
print(f"Total monsters killed: {killed_monsters}")
