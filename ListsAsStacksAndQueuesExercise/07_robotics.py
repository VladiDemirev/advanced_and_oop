from collections import deque

robot_data = input().split(";")
robot_name_time = [x.split("-") for x in robot_data]
hour, min, sec = [int(x) for x in input().split(":")]
start_time_sec = hour * 3600 + min * 60 + sec


def convert(start_time_sec):
    start_time_sec = start_time_sec % (24 * 3600)
    hour = start_time_sec // 3600
    start_time_sec %= 3600
    minutes = start_time_sec // 60
    start_time_sec %= 60
    return f"{hour:02d}:{minutes:02d}:{start_time_sec:02d}"


products = deque()
robots_products = {}
seconds_counter = 0
robot_busy_time = 0
robots_processing_busy_times = {}

for robot in robot_name_time:
    robots_processing_busy_times[robot[0]] = [int(robot[1]), robot_busy_time]

while True:
    command = input()
    if command == "End":
        break
    products.append(command)

while products:
    start_time_sec += 1
    for robot in robots_processing_busy_times:
        if robots_processing_busy_times[robot][1] <= start_time_sec:
            robots_products[robot] = f"{products.popleft()} [{convert(start_time_sec)}]"
            print(f"{robot} - {robots_products[robot]}")
            robots_processing_busy_times[robot][1] = start_time_sec + robots_processing_busy_times[robot][0]
            break
    else:
        products.rotate(-1)
