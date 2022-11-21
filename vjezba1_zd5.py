a = 184713
b = a % 86400 #ostatak sekundi u danima
c = a // 86400 #broj dana
d = b % 3600 #ostatak sekundi u satima
e = b // 3600 #broj sati
f = d % 60 #ostatak sekundi u minutama
g = d // 60 #broj minuta

print ("{} sekundi = {} dana, {} sata, {} minuta, {} sekundi".format(a,c,e,g,f))
