if __name__ == '__main__':
    f = open('testt', 'r')
    i = 0
    monkey = {0: [98, 89, 52], 1: [57, 95, 80, 92, 57, 78],
              2: [82, 74, 97, 75, 51, 92, 83], 3: [97, 88, 51, 68, 76],
              4: [63], 5: [94, 91, 51, 63], 6: [61, 54, 94, 71, 74, 68, 98, 83],
              7: [90, 56]}

    vizited0 = 0
    vizited1 = 0
    vizited2 = 0
    vizited3 = 0
    vizited4 = 0
    vizited5 = 0
    vizited6 = 0
    vizited7 = 0

    supermodel = 1

    for i in monkey:
        for j in monkey[i]:
            supermodel *= j

    for i in range(0, 10000):
        for j in monkey[0]:
            vizited0 += 1
            new = j * 2
            new2 = new % supermodel
            if new2 % 5 == 0:
                monkey[6].append(new2)
            else:
                monkey[1].append(new2)
        monkey[0] = []


        for j in monkey[1]:
            vizited1 += 1
            new = j * 13
            new2 = new % supermodel
            if new2 % 2 == 0:
                monkey[2].append(new2)
            else:
                monkey[6].append(new2)
        monkey[1] = []


        for j in monkey[2]:
            vizited2 += 1
            new = j + 5
            new2 = new % supermodel
            if new2 % 19 == 0:
                monkey[7].append(new2)
            else:
                monkey[5].append(new2)
        monkey[2] = []


        for j in monkey[3]:
            vizited3 += 1
            new = j + 6
            new2 = new % supermodel
            if new2 % 7 == 0:
                monkey[0].append(new2)
            else:
                monkey[4].append(new2)
        monkey[3] = []


        for j in monkey[4]:
            vizited4 += 1
            new = j + 1
            new2 = new % supermodel
            if new2 % 17 == 0:
                monkey[0].append(new2)
            else:
                monkey[1].append(new2)
        monkey[4] = []


        for j in monkey[5]:
            vizited5 += 1
            new = j + 4
            new2 = new % supermodel
            if new2 % 13 == 0:
                monkey[4].append(new2)
            else:
                monkey[3].append(new2)
        monkey[5] = []


        for j in monkey[6]:
            vizited6 += 1
            new = j + 2
            new2 = new % supermodel
            if new2 % 3 == 0:
                monkey[2].append(new2)
            else:
                monkey[7].append(new2)
        monkey[6] = []


        for j in monkey[7]:
            vizited7 += 1
            new = j * j
            new2 = new % supermodel
            if new2 % 11 == 0:
                monkey[3].append(new2)
            else:
                monkey[5].append(new2)
        monkey[7] = []




    print(0, vizited0)
    print(1, vizited1)
    print(2, vizited2)
    print(3, vizited3)
    print(4, vizited4)
    print(5, vizited5)
    print(6, vizited6)
    print(7, vizited7)






