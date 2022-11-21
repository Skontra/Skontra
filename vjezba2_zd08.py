x=int(input("Unesi troznamenkasti cijeli broj broja: "))
b1 , ost = divmod(x,100)
b2, b3 = divmod(ost,10)
print("%d \n%d \n%d" % (b1,b2,b3))
