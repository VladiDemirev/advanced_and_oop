# file = open("numbers.txt", "r")
# file.write("1\n2\n3\n4\n5")

import os

PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(PATH, "numbers.txt")

file = open(file_path)

result = 0
for line in file.readlines():
    result += int(line)
print(result)

file.close()
