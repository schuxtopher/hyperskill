class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = 1 / 2 * self.a * self.b
        self.is_right = self.c ** 2 == self.a ** 2 + self.b ** 2


sides = input().split(" ")
triangle = RightTriangle(int(sides[0]), int(sides[1]), int(sides[2]))

print(triangle.area if triangle.is_right else "Not right")
