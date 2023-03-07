

if __name__ == '__main__':
    f = open("test", "r")
    overlap = 0
    for line in f:
        line = line.replace(",",' ')
        line = line.replace('-', ' ')
        line = line.split(' ')

        a = int(line[0])
        b = int(line[1])
        c = int(line[2])
        d = int(line[3])

        if c <= b <= d:
            overlap = overlap + 1
        elif c <= a <= d:
            overlap = overlap + 1
        elif a <= c <= b:
            overlap = overlap + 1
        elif a <= d <= b:
            overlap = overlap + 1

    print(overlap)

