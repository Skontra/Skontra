l = []
l2 = []
n = int(input("Unesi: "))
if n < 0:
    n = -1*(n)
for i in range (1,n+1):
    if n % i == 0:
        if i % 2 == 1:
            l.append(-1*(i))
for i in range (1,n+1):
    if n % i == 0:
        if i % 2 == 0:
            l2.append(i)
l3 = l + l2
print(l)
print(l2)
print(l3)
for i in range (len(l3)):
    l3[i] = str(l3[i])
l3 = ','.join(l3)
print(l3)