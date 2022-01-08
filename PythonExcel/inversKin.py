import pylab
import math
import matplotlib.pyplot as plt
import numpy as np

a1 = 5
q1 = 32
a2 = 5
q2 = 62

# rad =  (alfa*math.pi)/180
# rad2=  ((alfa-beta)*math.pi)/180
rad = math.radians(q1)
rad2 = math.radians(q1 - q2)

x1 = [0, (a1 * math.cos(rad)), (a2 * math.cos(rad2)) + (a1 * math.cos(rad))]
y1 = [0, (a1 * math.sin(rad)), (a2 * math.sin(rad2)) + (a1 * math.sin(rad))]
x = 6
y = 6
l = math.sqrt(x * x + y * y)

q2 = math.acos(((x * x) + (y * y) - (a1 * a1) - (a2 * a2)) / (2 * a1 * a2))
q1 = math.atan2(y, x) - math.atan2((a2 * math.sin(q2)), (a1 + a2 * math.cos(q2)))
x21 = [0, (a1 * math.cos(q1)), (a2 * math.cos(q2)) + (a1 * math.cos(q1))]
y21 = [0, (a1 * math.sin(q1)), (a2 * math.sin(q2)) + (a1 * math.sin(q1))]

q21 = -math.acos(((x * x) + (y * y) - (a1 * a1) - (a2 * a2)) / (2 * a1 * a2))
q11 = math.atan2(y, x) + math.atan2((a2 * math.sin(q21)), (a1 + a2 * math.cos(q21)))
# q11=-q11
x11 = [0, (a1 * math.cos(q11)), (a2 * math.cos(q21)) + (a1 * math.cos(q11))]
y11 = [0, (a1 * math.sin(q11)), (a2 * math.sin(q21)) + (a1 * math.sin(q11))]

print(f"alfa= {math.degrees(q1)} beta = {math.degrees(q2)}  x= {x21[2]}  y= {y21[2]} l= {l}")
print(f"alfa= {math.degrees(q11)} beta = {math.degrees(q21)}  x= {x11[2]}  y= {y11[2]} l= {l}")

fig, axs = plt.subplots(3)
axs[0].plot(x21, y21)
axs[0].set_xlim([-20, 20])
axs[0].set_ylim([-10, 10])

axs[1].plot(x11, y11)
axs[1].set_xlim([-20, 20])
axs[1].set_ylim([-10, 10])

axs[2].plot(x1, y1)
axs[2].set_xlim([-20, 20])
axs[2].set_ylim([-10, 10])
plt.show()
