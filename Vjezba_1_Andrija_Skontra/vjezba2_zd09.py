x = int(input("Unesi cetveroznamenkasti cijeli broj: "))
b1 , ost1 = divmod(x,1000)
b2, ost2 = divmod(ost1,100)
b3, b4 = divmod(ost2, 10)
print("%d%d%d%d" % (b4,b3,b2,b1))
