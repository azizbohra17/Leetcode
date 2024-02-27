def divide(dividend, divisor):
        constraint = 2**31
        if dividend == -constraint and divisor == 1:
            return -constraint
        if dividend == -constraint and divisor == -1:
            return constraint - 1
        quotient = int(dividend / divisor)
        return quotient

# print(divide(-2147483648, -1))
