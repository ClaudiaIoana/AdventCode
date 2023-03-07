from collections import defaultdict

if __name__ == '__main__':
    f = open("test", "r")
    dir = defaultdict(int)
    path = []
    for line in f:
        line = line.rstrip()
        line = line.split()
        if line[1] == 'cd' and line[2] == "..":
            path.pop()
        elif line[1] == 'cd':
            path.append(line[2])
        elif line[1] != 'ls':
            if(line[0] != 'dir'):
                for i in range(0, len(path)):
                    dir[tuple(path[:i + 1])] += int(line[0])

    sum = 0
    index = 0
    used = 0
    for i in dir.values():
        if index == 0:
            used = i
        if(i <= 100000):
            sum = sum + i
        index += 1
    print(sum)

    unused = 70000000 - used
    needed = 30000000 - unused
    min = unused

    for i in dir.values():
        if needed <= i < min:
            min = i

    print(min)
