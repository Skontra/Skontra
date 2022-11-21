n = int(input("Unesi jedan cijeli broj veći od jedan: "))
lista = []
lista2 = []
print(lista)
if n > 1:
    for i in range(n+1):
        z = i % 2
        if z == 0:
            lista.append(i)
    print(lista)
    for i in range(n+1):
        z = i % 2
        if z == 1:
            lista2.append(i)
    print(lista2)
    lista3 = lista + lista2
    lista3.sort()
    print("Naša konačna lista izgleda ovako:",lista3)
else:
    print("Netočan unos.")