def basic_op(operator, value1, value2):
    if operator == '+':
        return (value1 + value2)
    elif operator == '-':
        return (value1 - value2)
    elif operator == '*':
        return (value1 * value2)
    elif operator == '/':
        return (value1 / value2)
#return eval(str(value1) + operator + str(value2))




def main():
    print(basic_op('+', 4, 7))
    print(basic_op('-', 15, 18))
    print(basic_op('*', 5, 5))
    print(basic_op('/', 49, 7))

main()
