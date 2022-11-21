a = float(input("unesi prvi decimalni broj:"))
b = float(input("unesi drugi decimalni broj:"))
c = a/b
c = int(c)
print("Suma", a, "i", b, "je", round(a+b,1), ".\nNjihova razlika je",round(a-b,1),"\nNjihov umnozak je",round(a*b,3),"\nNjihov kvocijent je",round(a/b,3),"\nNjihov cijelobrojni kvocijent je",c,"\nNjihov ostatak pri cijelobrojnom dijeljenju je",a%b)
