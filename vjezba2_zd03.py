a = float(input("Unesi duljinu u centimetrima:"))

b = a * 0.032808399
c = int(b) #stope cijelobrojna vrijednost
d = b - c
d = d * 12
d = int(d) #cijelovrojna vrijednost inca

print("zadanu duljina od {} centimetara je jednaka duljini {} stopa i {} inca" .format(a,c,d))

