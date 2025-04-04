"""
Formula of Falling Body: dv/dt = g - c * v^2 / m
if c = 0.225, m = 90, s = c/m

Body is falling free: at t = 0,  v(0) = 0

4. Degree Runge Kutta Formula;
y1 = y0 + 1/6(k1 + 2k2 + 2k3+ k4)
"""
from scipy.constants import constants
import matplotlib.pyplot as plt
g = constants.g
c, m = 0.225, 90
s = c/m
def runge_kutta(dvdt, v, t, h):
    k1 = h * dvdt(v, t)
    k2 = h * dvdt(v + 0.5*h, t + 0.5*k1)
    k3 = h * dvdt(v + 0.5*h, t + 0.5*k2)
    k4 = h * dvdt(v + h, t + k3)

    v = v + 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    t += h
    return t, v
def dvdt(v, t):
    return g - (s * v**2)

t0 = 0
v0 = 0
h = 0.1
t1 = 2

t_rk = [t0]
v_rk = [v0]
v = v0
t = t0
while t <= t1:
    t, v = runge_kutta(dvdt, v, t, h)
    t_rk.append(t)
    v_rk.append(v)
plt.figure(figsize=(7, 5))

plt.plot(t_rk, v_rk, label = "4. Dereceden Runge Kutta", dashes=(3,2), color="blue",
        lw=3)

plt.legend(loc="best", fontsize=12)
plt.title(r"Şu denklemin grafiği: $\quad\frac{dv}{dt}=g-(c/m)v^2$")
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.show()

print("Çözüm:", runge_kutta(dvdt, v, t, h))




