from collections import deque


def liters_wanted(liters, quantity, people_queue):
    person = people_queue.popleft()
    if liters <= quantity:
        return f"{person} got water"
    else:
        return f"{person} must wait"


def refill(liters, quantity):
    quantity += liters
    return quantity


def water_dispenser(quantity):
    people_queue = deque()
    name = input()
    while name != "Start":
        people_queue.append(name)
        name = input()
    command = input()
    while command != "End":
        action = command.split()
        if len(action) == 1:
            liters = int(action[0])
            print(liters_wanted(liters, quantity, people_queue))
            if quantity >= liters:
                quantity -= liters
        else:
            liters = int(action[1])
            quantity = refill(liters, quantity)
        command = input()
    return f"{quantity} liters left"


initial_quantity = int(input())
print(water_dispenser(initial_quantity))
