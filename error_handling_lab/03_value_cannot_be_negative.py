class ValueCannotBeNegative(Exception):
    pass


n = 5

for _ in range(n):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative
