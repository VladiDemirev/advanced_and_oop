def reversed_string(text):
    reversed_string = []
    for word in reversed(text):
        reversed_word = word[::-1]
        reversed_string.append(reversed_word)
    return " ".join(reversed_string)


input_text = input().split()
print(reversed_string(input_text))

# OPTION 2

# def reversed_string(text):
#   reversed_string = []
#   for i in range(len(text)):
#     reversed_string.append(text.pop())
#   return "".join(reversed_string)


# input_text = list(input())
# print(reversed_string(input_text))
