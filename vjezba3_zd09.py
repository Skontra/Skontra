sl = str(input("Unesi neko slovo engleske abecede: "))
sl = ord(sl)
if sl>64 and sl<123:
    print("Ovo slovo pripada engleskoj abecedi i ASCII kod mu je ",sl)
else:
    print("Ovo slovo ne pripada engleskoj abecedi")