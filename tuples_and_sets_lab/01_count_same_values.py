def count_same_values(input_numbers):
    occurances = {}
    for num in input_numbers:
        if num not in occurances:
            occurances[num] = input_numbers.count(num)
            print(f"{num} - {input_numbers.count(num)} times")

  # for number, count in occurances.items():
  #   print(f"{number} - {count} times")


numbers = tuple([float(x) for x in input().split()])
count_same_values(numbers)