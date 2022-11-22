for i in "abcd":
    for j in "abcd":
        for k in "abcd":
            for l in "abcd":
                if i != j and i != k and i != l:
                    if j != k and j != l:
                        if k != l:
                            print(i,j,k,l)
