import math


def heron(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


print(heron(int(input()), int(input()), int(input())))
