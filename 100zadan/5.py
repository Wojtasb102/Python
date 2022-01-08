class StrOperation:


    def __init__ (self):
        self.s = self.getString()

    def getString(self):
        s = input("Podaj Stringa: ")
        return str(s)

    def printString(self):
        print(self.s.upper())


ciag = StrOperation()
ciag.printString()
