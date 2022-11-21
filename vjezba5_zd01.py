n = int(input("Unesi prirodan broj: "))
niz = []
niz2 = []
niz3 = []
niz4 = []
for i in range (n):
    niz.append(i)
print("Naš niz:",*niz,sep=" ")
for i in range (n):
    if i % 2 == 1:
        niz2.append(i)
print("Naš niz kad uzmemo samo neparne brojeve:",*niz2,sep=" ")
umn = 1
for i in range (1,n+1):
    umn = umn*(i)
print("Faktorijela unesenoga broja:",umn)
if n % 2 == 0:
    for i in range (n):
        if (i+1)%2==0:
            niz3.append(i+1)
    print(niz3)
else:
    for i in range (n):
        if (i+1)%2==1:
            niz4.append(i+1)
    print(niz4)

