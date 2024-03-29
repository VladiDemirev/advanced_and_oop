class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.end_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.end_index:
            raise StopIteration()
        index = self.count
        self.count -= 1
        return index


#   TEST CODE

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

print()

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")
