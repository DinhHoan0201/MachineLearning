def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def get_precedence(operator):
    if operator == '^':
        return 3
    elif operator in ['*', '/']:
        return 2
    elif operator in ['+', '-']:
        return 1
    return 0


def infix_to_postfix(infix_expression):
    output = []
    operators = []
    tokens = infix_expression.split()

    for token in tokens:
        if token.isalnum():
            output.append(token)  # Nếu là chữ cái hoặc số, thêm vào kết quả cuối cùng
        elif token == '(':
            operators.append(token)  # Nếu là dấu mở ngoặc, đẩy vào stack toán tử
        elif token == ')':
            # Khi gặp dấu đóng ngoặc, đẩy các toán tử từ stack ra kết quả cuối cùng
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Loại bỏ dấu mở ngoặc
        elif is_operator(token):
            # Xử lý toán tử, đẩy các toán tử có độ ưu tiên cao hơn hoặc bằng vào stack
            while operators and operators[-1] != '(' and get_precedence(operators[-1]) >= get_precedence(token):
                output.append(operators.pop())
            operators.append(token)

    # Đẩy toán tử còn lại từ stack vào kết quả cuối cùng
    while operators:
        output.append(operators.pop())

    return ' '.join(output)


# Biểu thức trung tố đầu vào
infix_expression = "A/B + C*D*(E - F^G) - (H*I + K/L)^M"
postfix_expression = infix_to_postfix(infix_expression)
print("Biểu thức hậu tố: ", postfix_expression)
