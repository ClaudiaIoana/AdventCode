
if __name__ == '__main__':
    f = open('test', 'r')
    cycle = 0
    x = 1
    strength = 20
    final = 0
    for line in f:
        line = line.rstrip()
        line = line.split()
        if line[0] == 'noop':
            cycle += 1
        if line[0] == 'addx':
            cycle += 2

        if cycle >= strength:
            final += strength * x
            print(strength, strength* x, x)
            strength += 40
        if line[0] == 'addx':
            x += int(line[1])
            print(x)

    print(final)