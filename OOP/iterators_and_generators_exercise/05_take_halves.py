def solution():
    def integers():
        num = 1
        while True:
            yield num
            num += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]
        # sequence = []
        # for _ in range(n):
        #     sequence.append(next(seq))
        # return sequence

    return (take, halves, integers)


#   TEST CODE

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

print()

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))
