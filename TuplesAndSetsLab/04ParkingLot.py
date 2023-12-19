def parking_lot(commands_count):
    cars = set()
    for _ in range(commands_count):
        direction, plate = input().split(", ")
        if direction == "IN":
            cars.add(plate)
        elif direction == "OUT":
            cars.remove(plate)
    if cars:
        print(*cars, sep="\n")
    else:
        print("Parking Lot is Empty")


commands_number = int(input())
parking_lot(commands_number)
