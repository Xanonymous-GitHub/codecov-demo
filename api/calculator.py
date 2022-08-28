class Calculator:
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        try:
            return x * 1.0 / y
        except ZeroDivisionError:
            return 'Cannot divide by 0'