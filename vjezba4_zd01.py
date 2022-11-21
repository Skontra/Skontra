rj = str(input("Unesi bilo koji niz znakova: "))
duljina = len(rj)
print(max(rj))
print(min(rj))
if duljina > 1:
    print(rj[1])
else:
    print("String ima manje od 2 znaka te nije moguće izvršiti operaciju.")
print(rj[(duljina - 1)])
print("{}.{}.{}".format(rj,rj,rj))
if duljina > 1:
    z = rj[1:-1]
    print(z)
else:
    print("String ima manje od 2 znaka te nije moguće izvršiti operaciju.")
print(rj[::-1])
print(rj[::2])
if "a" in rj:
    print("U stringu postoji slovo a, te se nalazi na {}. mjestu.".format((rj.find('a')+1)))
else:
    print("U stringu ne postoji slovo a")
