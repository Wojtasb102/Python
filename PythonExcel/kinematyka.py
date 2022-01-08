import matplotlib.pyplot as plt
import numpy as np
from math import *

l1 = 5
l2 = 5
alfa = radians(12)
beta = radians(16)  # +alfa
betap = beta - alfa

xpoints = np.array([0, l1 * cos(alfa), l1 * cos(alfa) + l2 * cos(beta)])
ypoints = np.array([0, l1 * sin(alfa), l1 * sin(alfa) + l2 * sin(beta)])

x = xpoints[2]
y = ypoints[2]

q2 = -acos((pow(x, 2) + pow(y, 2) - pow(l1, 2) - pow(l2, 2)) / (2 * l1 * l2))
if q2 > 0:
    q2 = -q2
    q1 = atan2(x, y) + atan2((l2 * sin(q2)), (l1 + l2 * cos(q2)))
else:
    q2 = -q2
    q1 = atan2(x, y) - atan2((l2 * sin(q2)), (l1 + l2 * cos(q2)))
q2p = q2 + q1
ikX = np.array([0, l1 * cos(q1), l1 * cos(q1) + l2 * cos(q2p)])
ikY = np.array([0, l1 * sin(q1), l1 * sin(q1) + l2 * sin(q2p)])

print(f"q1 = {degrees(alfa):.2f}   q2 = {degrees(betap):.2f}")
print(f"q1 = {degrees(q1):.2f}   q2 = {degrees(q2):.2f}")

plt.subplot(211)
ax = plt.subplot(2, 2, 1)
plt.grid()
ax.plot(xpoints, ypoints)
ax2 = plt.subplot(2, 2, 2)
plt.grid()
ax2.plot(ikX, ikY)

plt.show()
