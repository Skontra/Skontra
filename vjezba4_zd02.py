x = str(input("Unesi bilo koji niz znakova: "))
y = int(input("Unesi jedan cijeli broj. "))
y += 1
if str(y) in x:
    print("Uneseni dio je u riječi")
else:
    print("Uneseni broj nije u riječi")