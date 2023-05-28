def intToRoman(num):
    roman = ''
    roman_char = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    dec_char = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    pointer = 0
    while num > 0:
        while num >= dec_char[pointer]:
            roman += roman_char[pointer]
            num -= dec_char[pointer]
        pointer += 1

    return roman


print(intToRoman(1994))

# OPTIMIZED APPROACH!
# def intToRoman(self, num: int) -> str:
#     roman = ''
#     roman_char = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
#     dec_char = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
#     for pointer in range(len(roman_char)):
#         if num // dec_char[pointer]:
#             count = num // dec_char[pointer]
#             roman += roman_char[pointer] * count
#             num = num % dec_char[pointer]
#     return roman
