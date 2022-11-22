n = int(input("Unesi neki broj: "))
m = int(input("Unesi neki broj: "))
x = m*n
for i in range(1,x+1):
    if i % n == 0 and i % m == 0:
        print(i)
        break