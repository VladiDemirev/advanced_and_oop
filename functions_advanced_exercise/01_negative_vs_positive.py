sequence = [int(x) for x in input().split()]

negatives_sum = sum([num for num in sequence if num < 0])
positives_sum = sum([num for num in sequence if num > 0])

print(negatives_sum)
print(positives_sum)
print("The negatives are stronger than the positives" if abs(negatives_sum) > positives_sum
      else "The positives are stronger than the negatives")
