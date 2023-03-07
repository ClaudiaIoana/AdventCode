

if __name__ == '__main__':
    f = open("test", "r")
    max1 = 0
    max2 = 0
    max3 = 0
    sum = 0
    nr = 1
    nr_max = 1
    for line in f:
        if line != '\n':
            sum = sum + int(line)
        elif line == '\n':
            nr = nr+1
            if sum > max1:
                max3 = max2
                max2 = max1
                max1 = sum
            elif sum > max2:
                max3 = max2
                max2 = sum
            elif sum> max3:
                max3 = sum
            sum = 0

    print(max1+max2+max3)
