def cache(func):
    def wrapper(n):
        # if n not in wrapper.log:
        if not wrapper.log.get(n):
            wrapper.log[n] = func(n)
        return wrapper.log[n]

    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


#  Test Code

fibonacci(3)
print(fibonacci.log)
print()
fibonacci(4)
print(fibonacci.log)
