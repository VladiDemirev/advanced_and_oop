# unique_usernames = {input() for i in range(int(input()))}
# print(*unique_usernames, sep="\n")


# OPTION 2

def unique_usernames(usernames):
    names = set()
    for i in range(usernames):
        username = input()
        names.add(username)
    print(*names, sep="\n")


num_usernames = int(input())
unique_usernames(num_usernames)
