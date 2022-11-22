x = str(input("Unesi:"))
x = [*x]
x.reverse()
print(x)
for i in range(len(x)):
    if x[i] == ",":
        x[i] = "."
x = ''.join(x)
print(x)
