import math
import matplotlib
import pylab


class Kine2:

    def calcAngle(self, reqcos):
        res1 = math.atan2(math.sqrt(1 - math.pow(reqcos, 2)), reqcos)
        res2 = math.atan2(math.sqrt(1 - math.pow(reqcos, 2)) * (-1), reqcos)
        return (res1, res2)

    def inputCalc(self):
        px = 11#float(input("px:"))
        py = 4#float(input("py:"))
        l1 = 10#float(input("l1:"))
        l2 = 5#float(input("l2:"))
        ctheta2 = (px ** 2 + py ** 2 - l1 ** 2 - l2 ** 2) / (2 * l1 * l2)
        stheta2 = math.sqrt(1 - math.pow(ctheta2, 2))
        ctheta1 = (px * (l1 + l2 * ctheta2) + py * l2 * stheta2) / (px ** 2 + py ** 2)
        theta1a, theta1b = self.calcAngle(ctheta1)
        theta2a, theta2b = self.calcAngle(ctheta2)

        x = [0, (l1 * math.sin(theta1a)), (l2 * math.sin(theta2a)) + (l1 * math.sin(theta1a))]
        y = [0, (l1 * math.cos(theta1a)), (l2 * math.cos(theta2a)) + (l1 * math.cos(theta1a))]

        xx = [0, (l1 * math.sin(theta1b)), (l2 * math.sin(theta2b)) + (l1 * math.sin(theta1b))]
        yy = [0, (l1 * math.cos(theta1b)), (l2 * math.cos(theta2b)) + (l1 * math.cos(theta1b))]

        print("theta1: {} and {} x:{} y:{}".format(math.degrees(theta1a), math.degrees(theta1b), x[2],y[2]))
        print("theta2: {} and {}".format(math.degrees(theta2a), math.degrees(theta2b)))
        pylab.plot(x, y, xx, yy)
        pylab.xlim(-10, 15)
        pylab.ylim(-10, 15)
        pylab.show()



kine2 = Kine2()
kine2.inputCalc()