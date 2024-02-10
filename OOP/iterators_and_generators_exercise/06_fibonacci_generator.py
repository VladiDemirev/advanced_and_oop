def fibonacci():
    current_num = 0
    next_num = 1
    # current_num, next_num = 0,1
    while True:
        yield current_num
        temp_num = current_num
        current_num = next_num
        next_num = temp_num + next_num
        # current_num, next_num = next_num, current_num + next_num


#  TEST CODE

generator = fibonacci()
for i in range(5):
    print(next(generator))

print()

generator = fibonacci()
for i in range(1):
    print(next(generator))
