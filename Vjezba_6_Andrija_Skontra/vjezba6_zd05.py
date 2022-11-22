x = str(input("Unesi:"))
x = [*x]
print(x)
x.pop()
x.append("+")
x.sort()
x = ''.join(x)
print(x)