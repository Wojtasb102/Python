x = input("Podaj liczby CSV: ")
X = x.split(',')

valueArray = []

for i in range (0, int(X[0])):
    array = []
    for j in range (0, int(X[1])):
        array.append(i*j)
    valueArray.append(array)
print (valueArray)
