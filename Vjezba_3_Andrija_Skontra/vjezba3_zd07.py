import math

baza = float(input("Unesi bazu: "))
arg = float(input("Unesi argument: "))
y = 0
if (arg > 0) & ((baza > 0) & (baza != 1)):
    y = math.log(arg, baza)
    print("Rijesenje logaritma je: ", y)
else:
    print("Rijesenje nije moguce")
