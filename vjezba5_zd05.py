zn = str(input("Unesi bilo koji niz znakova: "))
zn = [*zn] ##pretvara naš string u listu
l = []
print("U svim tim znakovima ovo su oni koji pripadaju hrvatskoj abecedi abecedi:\n")
for i in range(len(zn)):
    if (ord(zn[i]) > 64 and ord(zn[i]) < 91) or (ord(zn[i]) > 96 and ord(zn[i]) < 123) or (ord(zn[i]) == 381) or (ord(zn[i]) == 382) or (ord(zn[i]) == 353) or (ord(zn[i]) == 352) or (ord(zn[i]) == 268) or (ord(zn[i]) == 269) or (ord(zn[i]) == 262) or (ord(zn[i]) == 263) or (ord(zn[i]) == 272) or (ord(zn[i]) == 273): ##provjerava jeli znak u hrvatskoj abecedi
        l.append(zn[i])
for i in range(len(l)):
    if i != (len(l)):
        if (l[i] == "l" and l[i+1] == "j"):
            l[i] = [''.join(l[i: i+2])]
            l.pop(i+1)
for i in range(len(l)):
    if i != (len(l)):
        if (l[i] == "n" and l[i+1] == "j"):
            l[i] = [''.join(l[i: i+2])]
            l.pop(i+1)
for i in range(len(l)):
    if i != (len(l)):
        if (l[i] == "d" and l[i+1] == "ž"):
            l[i] = [''.join(l[i: i+2])]
            l.pop(i+1)
outputList = [x for l in l for x in l] ##nest-ane liste stavlja u listu
for i in range (len(outputList)):
    print(outputList[i])