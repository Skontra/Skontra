zn = str(input("Unesi bilo koji niz znakova: "))
zn = [*zn]
print("U svim tim znakovima ovo su oni koji pripadaju engleskoj abecedi:\n")
for i in range(len(zn)):
    if (ord(zn[i]) > 64 and ord(zn[i]) < 91) or (ord(zn[i]) > 96 and ord(zn[i]) < 123):
        print(zn[i])