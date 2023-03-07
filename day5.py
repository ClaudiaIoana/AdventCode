
if __name__ == '__main__':
    stacks = [[] for _ in range(1, 11)]
    stacks[1].extend(['R', 'N', 'P', 'G'])
    stacks[2].extend(['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H'])
    stacks[3].extend(['T', 'D', 'B', 'M', 'N', 'L'])
    stacks[4].extend(['R', 'V', 'P', 'S', 'B'])
    stacks[5].extend(['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H'])
    stacks[6].extend(['W', 'Q', 'S', 'C', 'D', 'B', 'J'])
    stacks[7].extend(['F', 'Q', 'L'])
    stacks[8].extend(['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V'])
    stacks[9].extend(['L', 'P', 'B', 'V', 'M', 'J', 'F'])

    stack = [[] for _ in range(1, 5)]
    stack[1].extend(['Z', 'N'])
    stack[2].extend(['M', 'C', 'D'])
    stack[3].extend(['P'])

    f = open('test', 'r')
    for line in f:
        line = line.split(' ')
        n = int(line[1])
        poz = int(line[3])
        poz2 = int(line[5])
        print(n, poz, poz2)
        print(stacks[poz], stacks[poz2])
        li = []
        for i in range(0, n):
            li.append(stacks[poz].pop(-1))

        for i in range(0, n):
            stacks[poz2].append(li.pop(-1))
            
        print(stacks[poz], stacks[poz2])



    for i in range(1, 11):
        print(stacks[i].pop(-1))
