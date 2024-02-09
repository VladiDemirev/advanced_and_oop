def squares(n):
    for num in range(1, n + 1):
        yield num ** 2


#   TEST CODE

print(list(squares(5)))