s = str(input("Unesi niz znakova: "))
s = [*s]
for i in range(len(s)):
    if s[i] == ' ':
        s[i] = "\n"
    if s[i] == '.':
        s[i] = " "
print(s)
x = ''.join(s)
print(x)