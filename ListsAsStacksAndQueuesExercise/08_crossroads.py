from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars_queue = deque()
total_cars_passed = 0

while True:
    command = input()
    if command == "END":
        break

    if command != "green":
        car = command
        cars_queue.append(car)
    else:
        remaining_green_light = green_light_duration
        while cars_queue and remaining_green_light > 0:
            car = cars_queue.popleft()
            if remaining_green_light < len(car):
                remaining_car = car[remaining_green_light:]
                cars_queue.appendleft(remaining_car)
                if free_window_duration >= len(remaining_car):
                    cars_queue.remove(remaining_car)
                    total_cars_passed += 1
                    break
                else:
                    print(f"A crash happened!\n{car} was hit at {remaining_car[free_window_duration]}.")
                    exit()
            else:
                remaining_green_light -= len(car)
                total_cars_passed += 1
                continue
print(f"Everyone is safe.\n{total_cars_passed} total cars passed the crossroads.")
