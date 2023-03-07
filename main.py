def dif(el, lista):
    occ = 0
    for i in range(0, 14):
        if el == lista[i]:
            occ = occ + 1
    if occ == 1:
        return True
    else:
        return False

if __name__ == '__main__':
    f = open('test', 'r')
    line = f.readline()
    ok = 1
    poz = 14
    while ok == 1:
        rez = True
        for i in range(0, 14):
            rez = rez and dif(line[i], line)
        if rez is True:
            ok = 0
        line = line[1:]
        poz = poz + 1
    print(poz - 1)