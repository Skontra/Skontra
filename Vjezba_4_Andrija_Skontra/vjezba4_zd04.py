a = str(input("Unesi bilo koje znakove: "))
b = len(a)
a = a[0:(len(a)):3]
print("Kad uzmemo svaki treći znak iz našeg unosa i stavimo razmak između dobijemo: " + " ".join(a))