

if __name__ == '__main__':
    f = open('test', 'r')
    vizible = 0
    lat = 0
    i = 0
    j = 0
    mat = [line.rstrip() for line in f]
    max = 0


    for i in range(1, len(mat)-1):
        for j in range(1, len(mat[i])-1):
            prod = 1
            nr = 0
            vizib = True
            for l in range(i-1, -1, -1):
                if vizib is True:
                    nr += 1
                if mat[i][j] <= mat[l][j]:
                    vizib = False
            if nr != 0:
                prod *= nr
                print(prod, nr)

            nr = 0
            viz = True
            for l in range(i+1, len(mat)):
                if viz is True:
                    nr += 1
                if mat[i][j] <= mat[l][j]:
                    viz = False
            if nr != 0:
                prod *= nr
                print(prod, nr)

            nr = 0
            vizib = vizib or viz
            viz = True
            for l in range(j-1, -1, -1):
                if viz is True:
                    nr += 1
                if mat[i][j] <= mat[i][l]:
                    viz = False
            if nr != 0:
                prod *= nr
                print(prod, nr)

            nr = 0
            vizib = vizib or viz
            viz = True
            for l in range(j+1, len(mat[0])):
                if viz is True:
                    nr += 1
                if mat[i][j] <= mat[i][l]:
                    viz = False
            if nr != 0:
                prod *= nr
                print(prod, nr)

            vizib = vizib or viz
            if vizib == True:
                vizible += 1

            print(prod)
            if max < prod:
                max = prod

    vizible += (len(mat) - 1 + len(mat[0]) - 1)*2
    print(max)



