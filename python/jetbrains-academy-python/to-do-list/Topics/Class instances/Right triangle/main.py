class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        if hyp ** 2 == leg_1 ** 2 + leg_2 ** 2:
            self.area = leg_1 * leg_2 / 2
            print("{0}".format(self.area))
        else:
            print("Not right")


input_c, input_a, input_b = [int(x) for x in input().split()]
triangle = RightTriangle(input_c, input_a, input_b)
