def possible_permutations(elements: list):
    if len(elements) <= 1:
        yield elements
    else:
        for i in range(len(elements)):
            current_el = elements[i]
            remaining_el = elements[:i] + elements[i + 1:]
            for p in possible_permutations(remaining_el):
                yield [current_el] + p


#   TEST CODE

# [print(n) for n in possible_permutations([1, 2, 3])]
for n in possible_permutations([1, 2, 3]):
    print(n)
print()
[print(n) for n in possible_permutations([1])]