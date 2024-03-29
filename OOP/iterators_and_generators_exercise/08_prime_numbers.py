def get_primes(integers: list):
    for num in integers:
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num


#   TEST CODE

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
print()
print(list(get_primes([-2, 0, 0, 1, 1, 0])))