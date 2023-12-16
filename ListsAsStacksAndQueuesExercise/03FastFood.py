# from collections import deque


# def biggest_order(orders_queue):
#   return max(orders_queue)


# def servicing(quantity, orders, orders_queue):
#   for order in orders:
#     if order > quantity:
#       break
#     else:
#       quantity -= order
#       orders_queue.popleft()
#   if orders_queue:
#     return f"Orders left: {' '.join(str(x) for x in orders_queue)}"
#   else:
#     return "Orders complete"


# daily_quantity = int(input())
# order_quantity = [int(x) for x in input().split()]
# queue = deque(order_quantity)

# print(biggest_order(queue))
# print(servicing(daily_quantity, order_quantity, queue))


# OPTION 2

# from collections import deque


# def biggest_order(orders):
#   return max(orders)


# def servicing(quantity, orders):
#   for order in orders.copy():
#     if order > quantity:
#       return f"Orders left: {' '.join(str(x) for x in orders)}"
#       break
#     else:
#       quantity -= order
#       orders.popleft()
#   else:
#     return "Orders complete"


# daily_quantity = int(input())
# order_quantity = deque(int(x) for x in input().split())

# print(biggest_order(order_quantity))
# print(servicing(daily_quantity, order_quantity))


# OPTION 3

from collections import deque


def biggest_order(orders):
    return max(orders)


def servicing(quantity, orders):
    for i in range(len(orders)):
        if orders[0] > quantity:
            return f"Orders left: {' '.join(str(x) for x in orders)}"
            break
        else:
            quantity -= orders[0]
            orders.popleft()
    else:
        return "Orders complete"


daily_quantity = int(input())
order_quantity = deque(int(x) for x in input().split())

print(biggest_order(order_quantity))
print(servicing(daily_quantity, order_quantity))
