n = int(input("Unesi broj koji pripada sustavu brojeva s bazom 5\n(sve znamenke moraju biti od 0 do 4): "))
m = n
l = []
for i in range(len(str(m))+1):
    l.append(n%5)
    n = n // 5
l.reverse()
for i in range(len(l)):
    l[i] = str(l[i])
l = ''.join(l)
print(l)


