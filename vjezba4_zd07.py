n = int(input("Unesi jedan cijeli broj veći od jedan: "))
lista = []
if n > 1:
    for i in range(n + 1):
        lista.append(i)
print("Naša orginalna lista:",lista)
lista2 = []
for i in range(n + 1):
     if (i % 2) == 0:
        lista2.append(i)
lista2.reverse()
print("Naša lista kad je obrnemo i ostavimo samo parne brojeve",lista2)

