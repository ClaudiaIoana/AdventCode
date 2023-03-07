#45
#150

if __name__ == '__main__':
    f = open('test', 'r')
    si = 0
    sj = 0
    ei = 0
    ej = 0
    i = 0
    matrix = [[0 for _ in range(0, 150)]for _ in range(0, 45)]
    for line in f:
        line = line.rstrip()
        for j in range(0, len(line)):
            if line[j] == 'S':
                si = i
                sj = j
            elif line[j] == 'E':
                ei = i
                ej = j
            matrix[i][j] = line[j]
        i += 1

    steps = 0
    while si != ei and sj != ej:
        

