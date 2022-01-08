import math


class Zespolona:
    def __init__ (self, re, im):
        self.re = re
        self.im = im

    def modul(self):
        mod = math.sqrt(self.re**2+self.im**2)
        return mod


image = Zespolona(3,2)
print(image.modul())