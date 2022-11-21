import math
a = float(input("Unesi prvu varijablu: "))
b = float(input("Unesi drugu varijablu: "))
c = float(input("Unesi trecu varijablu: "))
D = b*b - 4*a*c
if D>0:
    x1 = (-b+math.sqrt(b**2-(4*a*c)))/(2*a)
    x2 = (-b-math.sqrt(b**2-(4*a*c)))/(2*a)
    print ("Dva rijesenja", round(x1,4),round(x2,4))
elif D==0:
    print("Jedinstveno rijesenje: ", x1)
else:
    print("Rijesenje je kompleksno.")
