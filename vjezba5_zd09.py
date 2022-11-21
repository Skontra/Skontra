n = int(input("Unesi neki prirodni broj: "))
m = int(input("Unesi neki prirodni broj: "))
l = []
if n < m:
    for i in range(n+1,m,1):
        l.append(i)

if n > m:
    for i in range(m+1,n,1):
        l.append(i)

for i in range(len(l)):
    l[i] = str(l[i])

for i in range(len(l)):
    l[i] = list(l[i])

x = 0
y = 0
print("Brojevi sljedecih znamenki u datom rasponu koje zbrajanjem iznose 10.")
for i in range(len(l)):
    for j in range(len(l[i])):
        x = x + int((l[i])[j])
    if x == 10:
        y = ''.join(l[i])
        print(y)
    x = 0



