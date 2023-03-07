if __name__ == '__main__':
    f = open('test', 'r')
    lista = [0 for _ in range(1, 54)]
    suma = 0
    lines = 1
    final = 0

    for line1 in f:
        line1 = line1.rstrip()
        line2 = f.readline().rstrip()
        line3 = f.readline().rstrip()
        lista = [0 for _ in range(1, 54)]
        leni = len(line1)
        for i in range(0, leni):
            if 'a' <= line1[i] <= 'z':
                poz = ord(line1[i]) - ord('a') + 1
            else:
                poz = ord(line1[i]) - ord('A') + 27

            lista[poz] = 1

        leni = len(line2)
        for i in range(0, leni):
            if 'a' <= line2[i] <= 'z':
                poz = ord(line2[i]) - ord('a') + 1
            else:
                poz = ord(line2[i]) - ord('A') + 27

            if lista[poz] == 1:
                lista[poz] = 2

        leni = len(line3)
        for i in range(0, leni):
            if 'a' <= line3[i] <= 'z':
                poz = ord(line3[i]) - ord('a') + 1
            else:
                poz = ord(line3[i]) - ord('A') + 27

            if lista[poz] == 2:
                lista[poz] = 3
                suma = suma + poz

    print(suma)
