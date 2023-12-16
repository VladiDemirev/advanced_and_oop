from collections import deque


def is_balanced(parentheses):
    opening_parentheses = deque()
    while parentheses:
        current_bracket = parentheses.popleft()
        if current_bracket in '([{':
            opening_parentheses.append(current_bracket)
        elif not opening_parentheses:
            return "NO"
        else:
            if opening_parentheses.pop() + current_bracket not in "()[]{}":
                return "NO"
    return "YES"


parentheses_input = deque(input())
print(is_balanced(parentheses_input))
