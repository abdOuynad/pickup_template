def matrice_matrix(matrice,taile,k,client):
    matrix = []
    for row in range(taile):
        #
        m = []
        for col in range(taile):
            #
            #
            r = client - row * k
            c = client - col * k
            #
            #
            if (r >= k and c >= k):
                #
                for x in range(k):
                    a = []
                    for y in range(k):
                        a.append(matrice[row * k + x][col * k + y])
                    print(a)
                    m.append(a)
                print('----------')
                #
            elif (r >= k and c < k):
                #
                for x in range(k):
                    a = []
                    for y in range(k - c):
                        a.append(matrice[row * k + x][col * k + y])
                    print(a)
                    m.append(a)
                print('----------')
                #
            elif (r < k and c >= k):
                #
                for x in range(k - r):
                    a = []
                    for y in range(k):
                        a.append(matrice[row * k + x][col * k + y])
                    print(a)
                    m.append(a)
                print('----------')
                #
            elif (r < k and c < k):
                #
                for x in range(k - r):
                    a = []
                    for y in range(k - c):
                        a.append(matrice[row * k + x][col * k + y])
                    print(a)
                    m.append(a)
                print('----------')
                #
        print('m =>', m)
        matrix.append(m)
    print(matrix)
