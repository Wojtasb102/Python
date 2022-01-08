
myList=[]
for x in range(2000, 3201):
    if x % 5 == 0 and x % 7 != 0:
        myList.append(str(x))
print (','.join(myList))