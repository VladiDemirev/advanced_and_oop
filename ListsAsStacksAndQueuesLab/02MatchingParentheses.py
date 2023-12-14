def parentheses(expression):
    parentheses_expression = []
    bracket_indices = []
    for i in range(len(expression)):
        if expression[i] == "(":
            bracket_indices.append(i)
        if expression[i] == ")":
            current_expression = expression[bracket_indices.pop(): (i + 1)]
            parentheses_expression.append(current_expression)
    return '\n'.join(parentheses_expression)


# input_expression = list(input())
input_expression = input()
print(parentheses(input_expression))
