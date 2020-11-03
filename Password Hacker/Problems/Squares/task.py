n = int(input())


def squares():
    i = 1
    while True:
        yield i ** 2
        i += 1


gen = squares()

for _ in range(n):
    print(next(gen))
