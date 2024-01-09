def numbers(*args):
    sum_negatives = 0
    sum_positives = 0
    for num in args:
        if num < 0:
            sum_negatives += num
        elif num > 0:
            sum_positives += num
    print(sum_negatives)
    print(sum_positives)
    if abs(sum_negatives) > sum_positives:
        print("The negatives are stronger than the positives")
    elif abs(sum_negatives) < sum_positives:
        print("The positives are stronger than the negatives")


sequence = [int(x) for x in input().split()]
numbers(*sequence)
