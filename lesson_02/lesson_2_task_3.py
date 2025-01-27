import math


def square(x):
    return math.ceil(x*x)


num_x = float(input("Сторона квадрата = "))
print(f"S = {square(num_x)}")
