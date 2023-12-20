# def intersection(n_count, m_count):
#   set_n = {input() for i in range(n_count)}
#   set_m = {input() for i in range(m_count)}
#   # print(*(set_n & set_m), sep="\n") OR
#   mutual_elements = set_n.intersection(set_m)
#   print(*mutual_elements, sep="\n")


# n, m = [int(x) for x in input().split()]
# intersection(n, m)


#  OPTION 2

def intersection(n_count, m_count):
    set_n = {input() for i in range(n_count)}
    set_m = {input() for i in range(m_count)}
    mutual_elements = set_n.intersection(set_m)
    return mutual_elements


n, m = [int(x) for x in input().split()]
print(*intersection(n, m), sep="\n")
