import os

PATH = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(PATH, "test.txt")

with open(file_path) as f:

    replaced_chars = ["-", ",", ".", "!", "?"]

    for number, line in enumerate(f.readlines()):
        if number % 2 == 0:

            for char in replaced_chars:
                line = line.replace(char, "@")

            print(' '.join(reversed(line.split())))

