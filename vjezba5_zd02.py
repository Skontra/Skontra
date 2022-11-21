n = int(input("Unesi prirodan broj"))
brj = 0
for i in range (1,n+1):
    if n % i == 0:
        brj = brj +1
if brj == 2:
    print("Broj je prost")
else:
    print("Broj nije prost, te ima {} djeljitelja.".format(brj))


