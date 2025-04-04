"""
We can also find Pi within a hape that includes a rectangular volume and an ellipse in 3 dimensions. The volume of an
elliptical shape is found using the formula 4/3 * pi * (A*B*C). The volume of a rectangle is calculated as length *
width * height.
Let the volume of ellipse be Ve and the volume of the rectangle be Vr

So, let's say: Ve/Vd = 4/3 * pi * (A*B*C) / a*b*c -> Pi = 3 * Ve * a * b * c / (4 * Vd * A*B*C)

"""
from scipy.constants import constants as const
# Let's say: 3 values of elips is A, B, C and volume values of rectangles is a, b, c :
A, B, C = 1, 2, 3
a, b, c = 2, 4, 6

def Ve(A, B, C):
    return 4/3 * const.pi * A * B * C

def Vr(a, b, c):
    return a * b * c

pi = (3 * Ve(A, B, C) * a * b * c) / (4 * Vr(a, b, c) * A * B * C)
print("Calculated pi:", pi, "Expected Pi", const.pi)




