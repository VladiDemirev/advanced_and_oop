from collections import deque


def math_operations(*args, **kwargs):
    operations = {
        "a": lambda a, y: a + y,
        "s": lambda s, y: s - y,
        "d": lambda d, y: d / y if y != 0 else d,
        "m": lambda m, y: m * y,
    }
    args = deque(args)
    while args:
        for op in operations.items():
            if not args:
                break
            kwargs[op[0]] = op[1](kwargs[op[0]], args.popleft())
    sorted_dict = sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    result = "\n".join([f'{pair[0]}: {pair[1]:.1f}' for pair in sorted_dict])
    return result


#  TEST CODE

print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print()
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print()
print(math_operations(6.0, a=0, s=0, d=5, m=0))
