import os
from string import punctuation

PATH = os.path.dirname(os.path.abspath(__file__))
file_path_input = os.path.join(PATH, "text.txt")
file_path_output = os.path.join(PATH, "output.txt")
final_result = ""

with open(file_path_input) as f, open(file_path_output, "w") as output_file:

    result = []

    for row, line in enumerate(f):
        word_count = 0
        punctuation = 0

        for char in line:
            if char.isalpha():
                word_count += 1

            elif not char.isdigit() and char not in (" ", "\n"):
            # elif char in punctuation:
                punctuation += 1

        result.append(f"Line {row + 1}: {line[:-1]} ({word_count})({punctuation})")

    output_file.write('\n'.join(result))
