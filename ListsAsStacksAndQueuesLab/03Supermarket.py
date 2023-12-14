from collections import deque


def customers(command):
    clients_list = deque()
    while command != "End":
        if command == "Paid":
            while clients_list:
                print(clients_list.popleft())
        else:
            clients_list.append(command)
        command = input()
    return f"{len(clients_list)} people remaining."


name = input()
print(customers(name))

