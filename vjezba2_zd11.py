import math
a = float(input("Unesi koeficjent a: "))
b = float(input("Unesi koeficjent b: "))
c = float(input("Unesi koeficjent c: "))
x1 = (-b+ math.sqrt(b*b-4*a*c))/2*a
x2 = (-b- math.sqrt(b*b-4*a*c))/2*a
print("Rijesenja su:\n%d\n%d" %(x1,x2))
