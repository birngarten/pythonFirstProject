def calculator():
        result = 0
        import math
        num1 = input("Enter first number:")
        operator = input("Operator(+, - , *, /):\n")
        num2 = input("Enter second number:")
        num1 = float(num1)
        num2 = float(num2)

        if operator == '+':
            result = num1 + num2

        elif operator == '-':
            result = num1 - num2

        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        print(result)


calculator()



