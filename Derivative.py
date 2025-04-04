import math
"""
f'''(x) = 3[f(x+h) - f(x-h) - 2f'(x)*h] / (h**3)

"""

func = lambda x: (x * math.cos(x)) - (x**2 * math.sin(x))


def deriv1(func, x, h=1e-9):
    return (func(x+h) - func(x-h)) / (2*h)


def deriv3(func, x , h=1e-9):
    return (3 * (func(x+h) - func(x-h) - 2 * h * deriv1(func, x))) / (h**3)


print(deriv3(func, 4))


