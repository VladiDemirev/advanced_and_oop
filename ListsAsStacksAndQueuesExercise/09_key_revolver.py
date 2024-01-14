from collections import deque

bullet_price = int(input())
barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
intelligence_value = int(input())
shots_fired = 0

while locks and bullets:
    bullet = bullets.pop()
    lock = locks[0]

    if lock < bullet:
        print("Ping!")
    else:
        print("Bang!")
        locks.popleft()

    shots_fired += 1
    if bullets and shots_fired % barrel_size == 0:
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. Earned ${intelligence_value - shots_fired * bullet_price}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
