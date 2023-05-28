def divide(dividend, divisor):
    constraint = 2**31
    print(constraint)
    if dividend <= (-constraint):
        return 2 ** 31 - 1
    quotient = int(dividend / divisor)
    return quotient


print(divide(-2147483648, -1))
