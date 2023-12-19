# unique_names = {input() for x in range(int(input()))}

# print(*unique_names, sep="\n")


# OPTION 2

def unique_names(num_names):
    names = set()
    for _ in range(num_names):
        names.add(input())
    print(*names, sep="\n")


names_count = int(input())
unique_names(names_count)
