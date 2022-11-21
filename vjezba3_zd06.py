x: int = int(input("Unesi cijeli broj: "))
y = int(input("Unesi broj baze u koji zeliš konvertirati zadani broj: "))
if (y == 2):
    result  = f'{x:0b}'
    print("Nakon konvertiranja zadani broj je: ", result)
elif (y == 8):
    result = x[1:]
    print("Nakon konvertiranja zadani broj je: ", result)
elif (y == 16):
    result =f'{x:x}'
    print("Nakon konvertiranja zadani broj je: ",result)
else:
    print("Broj baze nije ispravno unesen")

