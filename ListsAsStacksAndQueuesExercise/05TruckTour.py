# from collections import deque


# def petrol_pump(pumps_count):
#   circle_road = deque()
#   starting_position = 0
#   current_fuel = 0
#   for i in range(pumps_count):
#     args = [int(x) for x in input().split()]
#     circle_road.append(args)
#   circle_road_copy = circle_road.copy()
#   while circle_road_copy:
#     args = circle_road_copy.popleft()
#     fuel_amount = args[0]
#     distance = args[1]
#     current_fuel += fuel_amount
#     if current_fuel >= distance:
#       current_fuel -= distance
#     else:
#       starting_position += 1
#       current_fuel = 0
#       circle_road.append(circle_road.popleft())
#       circle_road_copy = circle_road.copy()
#   return starting_position


# num_pumps = int(input())
# print(petrol_pump(num_pumps))


from collections import deque


def petrol_pump(circle):
    starting_position = 0
    current_fuel = 0
    circle_copy = circle.copy()
    while circle_copy:
        args = circle_copy.popleft()
        fuel_amount = args[0]
        distance = args[1]
        current_fuel += fuel_amount
        if current_fuel >= distance:
            current_fuel -= distance
        else:
            starting_position += 1
            current_fuel = 0
            circle.rotate(-1)
            circle_copy = circle.copy()
    return starting_position


circle_road = deque([[int(x) for x in input().split()] for x in range(int(input()))])
print(petrol_pump(circle_road))
