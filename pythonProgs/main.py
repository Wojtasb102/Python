import math
class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def wyswietlDane(self):
        print("Paramter a: {}, paramter b: {}, paramter c: {}".format(self.a, self.b, self.c))

    def rozwiaz(self):
        x = {}
        delta = (self.b * self.b) - (4 * self.a * self.c)
        print(delta)
        if delta == 0:
            x1 = -self.b / 2 * self.a
            x = {'x': x1}

        if delta > 0:
            x1 = (-self.b + math.sqrt(delta)) / 2 * self.a
            x2 = (-self.b - math.sqrt(delta)) / 2 * self.a
            x = {'x1': x1, 'x2': x2}
        if delta < 0:
            x = {'x': "brak"}
        return x


def main():
    funkcja = FunkcjaKwadratowa(1, 2, 1)
    funkcja.wyswietlDane()
    print(funkcja.rozwiaz())


if __name__ == "__main__":
    main()
