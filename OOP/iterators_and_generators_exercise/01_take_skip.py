class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_index = 0
        self.end_index = count - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.end_index:
            raise StopIteration( )
        index = self.current_index
        self.current_index += 1
        return index * self.step


#   TEST CODE

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

numbers = take_skip(10, 5)
for number in numbers:
    print(number)
