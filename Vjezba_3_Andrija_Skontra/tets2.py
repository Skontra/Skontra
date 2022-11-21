txt = "kdshkds asvh bjrtbjrbjd cugcreguk jds Hdskdsk ds hkdsk jsk sdk sdksdfk sdfbk Ufbk jsfbksfjkb sPjsfjsfbk fbjkfjbf bjfbj fj fj f jf fj fjf jf fj fjk fjk f"
lista = txt.lower()
lista = lista.split(" ")
lista = sorted(lista)
for word in lista:
    if len(word)>3:
        print(word)