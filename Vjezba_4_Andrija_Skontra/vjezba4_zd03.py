a = str(input("Unesi bilo koje znakove: "))
n = int(input("Unesi jedan cijeli broj: "))
n = n + 1
if str(n) in a:
    print("broj {} se nalazi u našim znakovima.".format(str(n)))
else:
    print("broj {} se NE nalazi u našim znakovima.".format(str(n)))