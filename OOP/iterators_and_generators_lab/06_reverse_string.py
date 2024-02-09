def reverse_text(string):
    # reverse_string = string[::-1]
    # yield reverse_string
    current_index = len(string) - 1
    end_index = 0
    while current_index >= end_index:
        yield string[current_index]
        current_index -= 1



#   TEST CODE

for char in reverse_text("step"):
    print(char, end='')
