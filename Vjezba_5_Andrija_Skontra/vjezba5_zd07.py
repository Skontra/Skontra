n = 1

while n < 10 or n > 99:
    n = int(input("Unesi prirodni dvoznamenkasti broj: "))
    if n < 10 or n > 99:
        print("Netočan unos, probaj ponovno.")
a = []
for i in range(1,n,2):
    a.append(i)
b = []
for i in range (len(a)):
    b.append(0)

x = 0
for i in range (len(a)): ##ovdje radimo b reversani
    while (a[i] > 0):
        x = a[i] % 10
        b[i] = (b[i] * 10) + x
        a[i] = a[i] // 10

for i in range (len(b)): ##pretvaramo parne brojeve u 0
    if b[i] % 2 == 0:
        b[i]=0

for i in range (len(b)): ##pretvaramo brojeve koji nisu dvoznamenkasti u nulu
    if b[i] < 10:
        b[i]=0

b.sort()

b = [i for i in b if i != 0]

c = []
for i in range (len(b)):
    c.append(0)
y = 0
for i in range (len(b)): ##ovdje radimo c reversani
    while (b[i] > 0):
        y = b[i] % 10
        c[i] = (c[i] * 10) + y
        b[i] = b[i] // 10

c.sort()
##jos moramo listu pretvoriti u string
for i in range(len(c)):
    c[i] = str(c[i])
k = ','.join(c)
print(k)