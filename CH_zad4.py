s = str(input("Unesi niz znakova: "))
s = [*s]
tocka,zarez,razmak = 0,0,0
for i in range(len(s)):
    if s[i] == s[i].lower():
        s[i] = s[i].upper()
    else:
        s[i] = s[i].lower()
    if s[i] == ".":
        tocka = tocka + 1
    if s[i] == ",":
        zarez = zarez + 1
    if s[i] == " ":
        razmak = razmak + 1

print(s,razmak,tocka,zarez)
