n = int(input("Unesi jedan prirodan broj koji je veći od nule: "))
m = int(input("Unesi drugi prirodan broj koji je veći od nule: "))
nzd = 0
for i in range(1,m+1):
    if m % i == 0 and n % i == 0:
        nzd = i
print("Njihov najveći djeljitelj je:",nzd)


