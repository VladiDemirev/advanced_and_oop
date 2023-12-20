def battle_of_names(names_count):
    odd_set = set()
    even_set = set()
    for row in range(1, names_count + 1):
        name = input()
        # result = sum([ord(x) for x in name]) // row
        '''NO NEED FOR SQUARE BRACKETS because in such a way it first creates a list so is slower.'''
        result = sum(ord(x) for x in name) // row
        odd_set.add(result) if result % 2 != 0 else even_set.add(result)
    # if sum(odd_set) == sum(even_set):
    #   return f"{', '.join(str(x) for x in (odd_set | even_set))}"
    if sum(odd_set) > sum(even_set):
        return f"{', '.join(str(x) for x in (odd_set - even_set))}"
    elif sum(odd_set) < sum(even_set):
        return f"{', '.join(str(x) for x in (odd_set ^ even_set))}"


num_names = int(input())
print(battle_of_names(num_names))
