def f(x):
    if x > 2:
        return (x - 2) ** 2 + 1

    if x <= -2:
        return 1 - (x + 2) ** 2

    return -x / 2
