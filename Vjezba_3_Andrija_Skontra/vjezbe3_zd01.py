x = int(input("Unesi kordinatu x: "))
y = int(input("Unesi kordinatu y: "))
if (x > 0) & (y > 0):
    print("Točka se nalazi u prvom kvadrantu.")
elif (x < 0) & (y > 0):
    print("Točka se nalazi u drugom kvadrantu.")
elif (x > 0) & (y < 0):
    print("Točka se nalazi u cetvrtom kvadrantu.")
else:
    print ("Netocan unos: ")