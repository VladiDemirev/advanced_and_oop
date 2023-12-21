# def numbers(seq1, seq2, lines):
#     for _ in range(lines):
#         command = input().split()
#         if command[0] == "Add":
#             items_to_add_remove = command[2:]
#             seq1.update(items_to_add_remove) if command[1] == "First" else seq2.update(items_to_add_remove)
#         elif command[0] == "Remove":
#             items_to_add_remove = set(command[2:])
#             seq1.difference_update(items_to_add_remove) if command[1] == "First" else seq2.difference_update(
#                 items_to_add_remove)
#         else:
#             print("True") if seq1.issubset(seq2) or seq2.issubset(seq1) else print("False")
#     print(*sorted({int(x) for x in seq1}), sep=", ")
#     print(*sorted({int(x) for x in seq2}), sep=", ")
#
#
# sequence1 = set(input().split())
# sequence2 = set(input().split())
# num_lines = int(input())
#
# numbers(sequence1, sequence2, num_lines)


#   OPTION 2

sequence1 = set(input().split())
sequence2 = set(input().split())
num_lines = int(input())

map_functions = {
    "Add First": lambda x: [sequence1.add(el) for el in x],
    "Add Second": lambda x: [sequence2.add(el) for el in x],
    "Remove First": lambda x: [sequence1.discard(el) for el in x],
    "Remove Second": lambda x: [sequence2.discard(el) for el in x],
    "Check Subset": lambda x: print(sequence1.issubset(sequence2) or sequence2.issubset(sequence1))
}

for _ in range(num_lines):
    first_command, second_command, *data = input().split()
    command = first_command + " " + second_command
    map_functions[command](data)

print(*sorted({int(x) for x in sequence1}), sep=", ")
print(*sorted({int(x) for x in sequence2}), sep=", ")
