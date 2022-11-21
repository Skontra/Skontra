x = int(input("Unesi broj bodova: "))
if x < 60 :
    print("Ocjena nedovoljan.")
elif x > 60 and x < 70 :
    print("Ocjena dovoljan.")
elif x > 70 and x < 80 :
    print("Ocjena dobar.")
elif x > 80 and x < 90 :
    print("Ocjena vrlo dobar.")
elif x > 90 and x <= 100 :
    print("Ocjena odlican.")
else:
    print("Unos netocan!!!")


