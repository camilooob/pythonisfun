def basic_op(operator, value1, value2):
    if operator == '+':
        return (value1 + value2)
    elif operator == '-':
        return (value1 - value2)
    elif operator == '*':
        return (value1 * value2)
    elif operator == '/':
        return (value1 / value2)





def main():
    print(basic_op('+', 4, 7))         # Output: 11
	print(basic_op('-', 15, 18))       # Output: -3
	print(basic_op('*', 5, 5))         # Output: 25
	print(basic_op('/', 49, 7))        # Output: 7

main()
