def is_near(index_H, index_T):
    if index_T[0] - 1 == index_H[0] and index_T[1] == index_H[1]:
        return True
    if index_T[0] + 1 == index_H[0] and index_T[1] == index_H[1]:
        return True
    if index_T[1] - 1 == index_H[1] and index_T[0] == index_H[0]:
        return True
    if index_T[1] + 1 == index_H[1] and index_T[0] == index_H[0]:
        return True

    if index_T[0] - 1 == index_H[0] and index_T[1] - 1 == index_H[1]:
        return True
    if index_T[0] + 1 == index_H[0] and index_T[1] + 1 == index_H[1]:
        return True
    if index_T[1] - 1 == index_H[1] and index_T[0] + 1 == index_H[0]:
        return True
    if index_T[1] + 1 == index_H[1] and index_T[0] - 1 == index_H[0]:
        return True
    if index_T[0] == index_H[0] and index_T[1] == index_H[1]:
        return True
    return False

def inc_tail(index_H, index_T):
    pozi = (index_H[0] + index_T[0]) / 2
    pozj = (index_H[1] + index_T[1]) / 2

    if (pozi * 10) % 10 == 0 and (pozj * 10) % 10 == 0:
        index_T = [pozi, pozj]
    elif (pozi * 10) % 10 == 5 and (pozj * 10) % 10 == 0:
        index_T = [index_H[0], pozj]
    elif (pozi * 10) % 10 == 0 and (pozj * 10) % 10 == 5:
        index_T = [pozi, index_H[1]]
    elif (pozi * 10) % 10 == 5 and (pozj * 10) % 10 == 5:
        index_T = index_H

    return index_T

def inc_index(index_H, poz):
    if poz == 'U':
        index_H[0] += 1
    if poz == 'D':
        index_H[0] -= 1
    if poz == 'L':
        index_H[1] -= 1
    if poz == 'R':
        index_H[1] += 1
    return index_H



if __name__ == '__main__':
    f = open('test', 'r')
    index_H = [1000, 1000]
    index_T = [[1000, 1000] for _ in range(1, 11)]
    last_went = 'L'
    inc = 1
    vizited = []


    for line in f:
        line = line.split()
        #last_went = line[0]
        for i in range(0, int(line[1])):
            index_H = inc_index(index_H, line[0])
            if is_near(index_H, index_T[1]) is False:
                i9 = index_T[9]
                index_T[1] = inc_tail(index_H, index_T[1])
                for i in range(2, 10):
                    if is_near(index_T[i-1], index_T[i]) is False:
                        index_T[i] = inc_tail(index_T[i-1], index_T[i])
                if index_T[9] != i9:
                    if index_T[9] not in vizited:
                        vizited.append(index_T[9])
                        inc += 1
        last_went = line[0]

    print(inc)
#6480 - to high
#2504
