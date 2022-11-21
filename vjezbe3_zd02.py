import math

a = int(input("Unesi prvu stranicu trokuta: "))
b = int(input("Unesi drugu stranicu trokuta: "))
c = int(input("Unesi trecu stranicu trokuta: "))

if (a + b) > c and (b + c) > a and (a + c) > b:
    s = ((a + b + c)/2)
    P = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("Povrsina trokuta je: ",P)
else:
    print("ERROR")
