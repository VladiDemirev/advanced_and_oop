# file = open("words.txt", "w")
# file.write("quick is fault")
#
# file = open("input.txt", "w")
# file.write("-I was quick to judge him, but it wasn't his fault.\n"
#            "-Is this some kind of joke?! Is it?\n"
#            "-Quick, hide here…It is safer.\n")
#
# file = open("output.txt", "w")

import re

with open("words.txt", "r") as file:
    searched_words = file.read().lower().split()

with open("input.txt", "r") as file:
    text = file.read().lower()

file_two = open("output.txt", "w")

occurrences = {}

for word in searched_words:
    pattern = re.findall(rf"\b{word}\b", text)
    if word in text:
        occurrences[word] = len(pattern)

sorted_words = sorted(occurrences.items(), key=lambda kvp: -kvp[1])

with open("output.txt", "w") as file:
    for word, count in sorted_words:
        file.write(f"{word} - {count}\n")
