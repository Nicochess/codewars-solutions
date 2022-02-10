import math
def square_area(a):
    calc = ((a * 4 / math.pi) / 2) ** 2
    return float("{:.2f}".format(calc))