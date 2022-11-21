a = int(input("Unesi cijeli broj: "))
b = int(input("Unesi cijeli broj: "))
c = str(input("Unesi racunsku  operaciju (+,-,*,/): "))
if c == "+" :
    print("Njihov zbroj je: ",a+b)
elif c == "-" :
    print("Njihova razlika je: ",a-b)
elif c == "*" :
    print("Njihov umnozak je: ",a*b)
elif c == "/" :
    print("Njihov kolicnik je: ",a/b)
else:
    print("Nije dobar unos.")
