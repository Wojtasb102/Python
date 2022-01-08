import pylab
import math

l1 = 5
alfa = 45
l2 = 5
beta = -91

#rad =  (alfa*math.pi)/180
#rad2=  ((alfa-beta)*math.pi)/180
rad = math.radians(alfa)
rad2 = math.radians(alfa - beta)

x = [0, (l1 * math.sin(rad)), (l2 * math.sin(rad2)) + (l1 * math.sin(rad))]
y = [0, (l1 * math.cos(rad)), (l2 * math.cos(rad2)) + (l1 * math.cos(rad))]

l = math.sqrt(pow(x[2], 2) + pow(y[2], 2))

gamma = math.acos((pow(l, 2) - pow(l1, 2) - pow(l2, 2)) / (-2 * l1 * l2))
omega = math.atan(x[2] / y[2])
theta = math.acos((pow(l2, 2) - pow(l, 2) - pow(l1, 2)) / (-2 * l * l1))

betaperim = math.degrees(gamma) - 180
print(f"alfa= {math.degrees(omega - theta)} beta = {betaperim}  x= {x[2]}  y= {y[2]} l= {l}")
pylab.plot(x, y)
pylab.xlim(-10, 10)
pylab.ylim(-10, 10)
pylab.show()
