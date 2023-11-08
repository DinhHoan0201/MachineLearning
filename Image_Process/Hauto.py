def is_operator(c):
    return c in ['+', '-', '*', '/']
def perform_operation(operator, operand1, operand2):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2

def evaluate_postfix_expression(postfix):
    operands = []
    tokens = postfix.split()

    for token in tokens:
        if token.isdigit():
            operands.append(int(token))
        elif is_operator(token):
            operand2 = operands.pop()
            operand1 = operands.pop()
            result = perform_operation(token, operand1, operand2)
            operands.append(result)

    return operands[0]

# Đoạn mã chính
postfix_expression = "3 2 + 2 5 2 ^ + 4 1 + 7 - 9 + - *"
result = evaluate_postfix_expression(postfix_expression)
print("Giá trị của biểu thức hậu tố là:", result)
