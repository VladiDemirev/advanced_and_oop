from collections import deque

initial_fuel = [int(x) for x in input().split()]
consumption_idx = deque(int(x) for x in input().split())
needed_fuels = deque(int(x) for x in input().split())

altitude_reached = 0
altitudes = []

while altitude_reached <= 4:

    fuel_amount = initial_fuel.pop()
    fuel_index = consumption_idx.popleft()
    result = fuel_amount - fuel_index
    fuel_needed = needed_fuels.popleft()

    altitude_reached += 1

    if result >= fuel_needed:
        print(f"John has reached: Altitude {altitude_reached}")
        altitudes.append(f"Altitude {altitude_reached}")
    else:
        print(f"John did not reach: Altitude {altitude_reached}")
        if altitudes:
            print("John failed to reach the top.")
            print(f"Reached altitudes: {', '.join(altitudes)}")
        elif not altitudes:
            print("John failed to reach the top.")
            print("John didn't reach any altitude.")
        break

else:
    print("John has reached all the altitudes and managed to reach the top!")
