import math


def sigmoid(x):
    return 1 / (1 + math.pow(math.e, -x))


print(round(sigmoid(int(input())), 2))
