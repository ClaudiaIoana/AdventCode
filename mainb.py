
if __name__ == '__main__':
    f = open('test', 'r')
    cycle = 0
    x = 0
    strength = 40
    row = []
    i = 0

    for line in f:
        #print(line)
        line = line.rstrip()
        line = line.split()

        if line[0] == 'noop':
            if cycle == x or cycle == x + 1 or cycle == x + 2:
                row.append('#')
            else:
                row.append(".")
            cycle += 1
            #print(row[-1], cycle-1, x)
        if line[0] == 'addx':
            #print(cycle, )
            if cycle == x or cycle == x + 1 or cycle == x + 2:
                row.append('#')
            else:
                row.append(".")
            cycle += 1
            #print(row[-1], cycle-1, x)

            if cycle >= strength:
                print(*row)
                row = []
                cycle = 0
                #x = 0

            if cycle == x or cycle == x + 1 or cycle == x + 2:
                row.append('#')
            else:
                row.append(".")
            cycle += 1
            #print(row[-1], cycle-1, x)
            x = x + int(line[1])



        #print(row)
        if cycle >= strength:
            print(*row)
            row = []
            cycle = 0
            #x = 0

