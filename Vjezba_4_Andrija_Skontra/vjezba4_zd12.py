a = str(input("Unesi neki niz znamenaka: "))
b = list(a)
b= [eval(i) for i in b]
suma = sum(b)
sredina = round((suma / len(b)),4)
print("Artimetička sredina unesenih znamenaka je: ",sredina)