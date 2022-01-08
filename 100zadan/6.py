import math

x = input("Podaj liczby CSV: ")
D = x.split(',')

C = 50
H = 30
outputList = []

for x in D:
    Q = math.sqrt((2*C*int(x))/H) #Q = Square root of [(2 * C * D)/H]
    outputList.append(str(round(Q)))

print (','.join(outputList))
