import math

x = int(input())
y = int(input())

print(f"{math.log(x, y):.02f}" if y > 1 else f"{math.log(x):.02f}")
