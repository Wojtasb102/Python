def silnia(liczba):
    if liczba == 1:
        return 1
    else:
        return liczba * silnia (liczba-1)

x = int(input("podaj liczbe: "))
print(silnia(x))
