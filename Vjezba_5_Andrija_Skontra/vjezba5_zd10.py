n = int(input("Unesi bilo koji prirodni broj: "))
print("Prvi palidrom koji je jednak ili manji od našega broja je:")
l = []
for i in range(n,0,-1):
    l.append(i)

for i in range(len(l)):
    l[i] = str(l[i])

k = []
for i in range(len(l)):
    k.append((l[i])[::-1])

for i in range(len(l)):
    if l[i] == k[i]:
        print(k[i])
        break