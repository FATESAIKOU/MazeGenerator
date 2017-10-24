import random
import os
import sys
import numpy as np
from pprint import pprint


def getReachable(x, y, n, m, maze):
    eles = [
        (x, y + 1),
        (x + 1, y)
    ]

    next_set = set()
    for (nx, ny) in eles:
        if -1 < nx < n and -1 < ny < m and maze[nx][ny] == 0:
            next_set.add((nx, ny))

    return next_set

def isVisitable(x, y, n, m, maze):
    eles = [
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y)
    ]

    lnk_cnt = 0
    for (nx, ny) in eles:
        if -1 < nx < n and -1 < ny < m:
            lnk_cnt += maze[nx, ny]

    return lnk_cnt == 1
    

def genMaze(x, y, n, m):
    maze = np.zeros([n, m])
    
    nx, ny = x, y
    maze[nx][ny] = 1

    next_set = set()
    plen = random.randint(200, 200)
    while True:
        tmp_set = getReachable(nx, ny, n, m, maze);
        next_set = next_set.union(tmp_set)

        if len(next_set) == 0:
            break

        if plen > 0 and len(tmp_set) > 0:
            aim_set = tmp_set
            plen = plen - 1
        else:
            plen = random.randint(9, 10)
            aim_set = next_set

        nx, ny = random.sample(aim_set, 1)[0]
        next_set.discard((nx, ny))

        if isVisitable(nx, ny, n, m, maze):
            maze[nx][ny] = 1
        else:
            print >> sys.stderr, maze[nx][ny], (nx, ny)

    return maze

def printMaze(n, m, maze, draw_pair):
    print " " + "_"*m + " "
    for i in range(n):
        s = "|"
        for j in range(m):
            if maze[i, j] == 1:
                s = s + draw_pair[0]
            else:
                s = s + draw_pair[1]
        print s + "|"
    print " " + "-"*m + " "

printMaze(35, 140, genMaze(0, 0, 35, 140), ('1', '0'))
