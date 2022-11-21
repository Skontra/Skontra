from typing import List, Any

a = str(input("Unesi:"))
b: list[Any] = list(a)
d: list[Any] = list(a)
print("Broj svih razmaka u našoj listi je:",b.count(" "))
b.sort()
print("Naša sortirana lista bez zadnjeg znaka:",b[:len(b)-1])
z = "a"
if z in d:
    d.remove("a")
    print("Naša lista bez prvog slova a:",d)
else:
    print("nema slova a")