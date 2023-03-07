#rock = A, X = 1
#paper = B, Y = 2
#scrissors = C, Z = 3

#lose = 0
#draw = 3
#win = 6

if __name__ == '__main__':
    f = open("test", "r")
    points = 0
    lin = 0
    score = 0
    with open("test") as my_file:
        for lines in my_file:
            moves = lines.split()
            elfMove = moves[0]
            outcome = moves[1]
            if (outcome == "X"):
                # you lose => no additional points
                if (elfMove == "A"):
                    # elf = rock & you = scissors
                    score = score + 3
                if (elfMove == "B"):
                    # elf = paper & you = rock
                    score = score + 1
                if (elfMove == "C"):
                    # elf = scissors & you = paper
                    score = score + 2
            if (outcome == "Y"):
                score = score + 3
                if (elfMove == "A"):
                    # elf = rock & you = rock
                    score = score + 1
                if (elfMove == "B"):
                    # elf = paper & you = paper
                    score = score + 2
                if (elfMove == "C"):
                    # elf = scissors & you = scissors
                    score = score + 3
            if (outcome == "Z"):
                score = score + 6
                if (elfMove == "A"):
                    # elf = rock & you = paper
                    score = score + 2
                if (elfMove == "B"):
                    # elf = paper & you = scissors
                    score = score + 3
                if (elfMove == "C"):
                    # elf = scissors & you = rock
                    score = score + 1
    print(score)