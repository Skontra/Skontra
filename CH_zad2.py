m = int(input("Unesi: "))
n = int(input("Unesi: "))
if (m < 1) or (n < 1):
    print("Krivi unos.")
else:
    l = []
    for i in range(m):
        l.append(i)
    l.append(m)
    print(l)
    brojac = 0
    for i in range (0,len(l)):
        brojac = brojac + (float(l[i])/n)
    print(brojac)