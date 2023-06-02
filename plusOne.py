def plusOne(digits):
    size = len(digits)
    sum1 = 0
    new = []
    for i in range(size):
        sum1 = sum1 * 10 + digits[i]
    sum1 += 1
    temp = sum1
    for i in range(len(str(sum1))):
        dig = temp % 10
        new = [dig] + new
        temp = temp // 10
    return new

print(plusOne([9]))