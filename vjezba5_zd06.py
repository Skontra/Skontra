n = int(input("Unesite broj predmeta: "))
x = []
for i in range (n):
    x.append(10)
    while (x[i] <= 0) or (x[i] > 5):
        x[i] = int(input("Unesite ocjenu {}. predmeta: ".format(i+1)))
        if (x[i] <= 0) or (x[i] > 5):
            print("Neispravan unos, molimo pokušajte ponovno: ")
print(x)
suma = 0
if 1 in x:
    print("Nedovoljan")
else:
    for i in range(len(x)):
        suma = suma + x[i]
    print("Prosjek ocjena je:",suma/(len(x)))