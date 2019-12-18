def parse_expression(expression):
    tokens = expression.split()
    stack = []
    result = 0
    for token in tokens:
        if token.isdigit():
            stack.append(token)
        else:
            a = stack.pop()
            b = stack.pop()
            c = compute(a, b, token)
            stack.append(c)
            result = c

    print(result)
    return result


def compute(a, b, symbol):
    num_a, num_b = int(a), int(b)
    if symbol == '+':
        return num_b + num_a
    elif symbol == '-':
        return num_b - num_a
    elif symbol == '/':
        return num_b / num_a
    elif symbol == '*':
        return num_b * num_a
    else:
        raise SyntaxError(f'Unexpected token {symbol}')


assert parse_expression("2 5 +") == 7
assert parse_expression("5 2 -") == 3
assert parse_expression("5 1 2 + 4 * + 3 -") == 14
assert parse_expression("10 10 + 5 -") == 15

