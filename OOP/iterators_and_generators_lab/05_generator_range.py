def genrange(start: int, end: int):
    while start <= end:
        yield start
        start += 1


#   TEST CODE

print(list(genrange(1, 10)))