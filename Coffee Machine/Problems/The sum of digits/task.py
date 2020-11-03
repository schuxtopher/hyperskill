number = int(input())
digit_0 = number % 10
digit_1 = number // 10 % 10
digit_2 = number // 10 ** 2
print(digit_0 + digit_1 + digit_2)
