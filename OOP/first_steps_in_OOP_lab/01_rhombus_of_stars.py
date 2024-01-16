# n = int(input())

# for i in range(1, n + 1):
#   print(" " * (n - i), end="")
#   print(*["*"] * i)

# for j in range(n - 1, 0, -1):
#   print(" " * (n - j), end="")
#   print(*["*"] * j)


# SOLUTION WITH FUNCTIONS

def upper_part(size):
    for i in range(1, n + 1):
        print(" " * (n - i), end="")
        print(*["*"] * i)


def lower_part(size):
    for j in range(n - 1, 0, -1):
        print(" " * (n - j), end="")
        print(*["*"] * j)


def print_rhombus(size):
    upper_part(size)
    lower_part(size)


n = int(input())
# upper_part(n)
# lower_part(n)
print_rhombus(n)
