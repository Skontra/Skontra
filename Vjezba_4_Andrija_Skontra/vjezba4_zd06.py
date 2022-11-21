x =  str(input("Unesi bilo koje znakove: "))
y = str(input("Opet unesi bilo koje znakove: "))
l = len(y)
if y in x:
    print("Kad ispišemo sve znakove (prvog unosa) nakon onih koji se ponavljaju iz drugog unosa dobivamo ovo:",x[((x.find(y))+l):])
else:
    print("U prvom inputu nema ponavljanja drugog inputa.")