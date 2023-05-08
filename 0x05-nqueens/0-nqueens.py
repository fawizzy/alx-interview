#!/usr/bin/python3
from sys import argv

if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
else:
    argv[1] = int(argv[1])

if isinstance(argv[1], int) == False:
    print("N must be a number")
    exit(1)

if argv[1] < 4:
    print("N must be at least 4")
    exit(1)

sol = []
pos = [] # [row, col]
cols = set()
posDiag = set()
negDiag = set()




def backtrack(row):
    if row == argv[1]:
        # sol.append(pos)
        print("jytdr", row)
        return
    for col in range(argv[1]):
        pos = [row, col]
        # print(pos)
        dif = row - col
        if col in cols or sum(pos) in posDiag or dif in negDiag:
            # print("negDiag: ", negDiag)
            # print("posDiag: ", posDiag)
            # print("cols   : ", cols)
            # print("pos    : ", pos)
            print("")
            continue
        
        posDiag.add(sum(pos))
        negDiag.add(dif)
        cols.add(col)
        sol.append(pos)
        print("negDiag: ", negDiag)
        print("posDiag: ", posDiag)
        print("cols   : ", cols)
        print("pos    : ", pos)
        backtrack(row + 1)

        # posDiag.remove(sum(pos))
        # negDiag.remove(dif)
        # 
        # cols.remove(col)
    print("finished", row)
    return

        
backtrack(0)
print(sol)