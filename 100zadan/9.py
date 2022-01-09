line = []
while True:
    inStr = input("Podaj Stringa (wciśnij enter zaby zakończyć): ")
    if inStr:
        line.append(inStr.upper())
    else:
        break;

for sentence in line:
    print(sentence)
