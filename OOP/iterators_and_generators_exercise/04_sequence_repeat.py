#   OPTION 1


# class sequence_repeat:
#     def __init__(self, sequence: str, number: int):
#         self.sequence = sequence
#         self.number = number
#         self.current_index = 0
#         self.temp_position = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current_index > self.number - 1:
#             raise StopIteration()
#         position = self.current_index
#         self.current_index += 1
#         if position > len(self.sequence) - 1:
#             position = self.temp_position
#             self.temp_position += 1
#             if self.temp_position > len(self.sequence) - 1:
#                 self.temp_position = 0
#         return self.sequence[position]


#   OPTION 2

class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index > self.number - 1:
            raise StopIteration()
        position = self.current_index % len(self.sequence)
        self.current_index += 1
        return self.sequence[position]


#   TEST CODE

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

print()

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')
