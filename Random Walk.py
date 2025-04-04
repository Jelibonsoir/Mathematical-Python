"""
"What is Random Walk?

In mathematics, Random Walk refers to a stochastic process that describes a path consisting of a sequence of random steps
in certain mathematical spaces. In other words, the future position of an object is completely independent of its current
position. The simplest example of a Random Walk is a drunk person. A drunk person has no preferred direction, so moving
in any direction is equally likely. Integers can also serve as an example of this method; let's assume our current
position is 0, and our probabilities of moving forward and backward (positive and negative) are the same. Concepts like
Brownian Motion, a gambler's financial status, or the fluctuating price of a stock are also suitable examples to illustrate
this method.

"""

import matplotlib.pyplot as plt
import numpy as np
import random


def randomwalk(n):
    # Here, we created 3 arrays, each containing n zeros.
    a = np.zeros(n)
    b = np.zeros(n)
    c = np.zeros(n)
    # This list consists of the probabilities of moving in any directon witthin a 3D Space
    directions = ["UP", "DOWN", "RIGHT", "LEFT", "IN", "OUT"]
    for p in range(1, n):
        adım = random.choice(directions)
        if adım == "RIGHT":
            a[p] = a[p - 1] + 1
            b[p] = b[p - 1]
            c[p] = c[p - 1]
        elif adım == "LEFT":
            a[p] = a[p - 1] - 1
            b[p] = b[p - 1]
            c[p] = c[p - 1]
        elif adım == "UP":
            a[p] = a[p - 1]
            b[p] = b[p - 1] + 1
            c[p] = c[p - 1]
        elif adım == "DOWN":
            a[p] = a[p - 1]
            b[p] = b[p - 1] - 1
            c[p] = c[p - 1]
        elif adım == "IN":
            a[p] = a[p - 1]
            b[p] = b[p - 1]
            c[p] = c[p - 1] - 1
        elif adım == "OUT":
            a[p] = a[p - 1]
            b[p] = b[p - 1]
            c[p] = c[p - 1] + 1
    return a, b, c

a_data, b_data, c_data = randomwalk(10000)
ax = plt.subplot(1, 1, 1, projection='3d')
ax.plot(a_data, b_data, c_data, alpha=0.9)
ax.scatter(a_data[-1], b_data[-1], c_data[-1])
plt.show()

