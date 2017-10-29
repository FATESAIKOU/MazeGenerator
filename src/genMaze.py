import random
import os
import sys
import numpy as np
import time
from pprint import pprint


def getReachable(x, y, n, m, maze):
    eles = [
        (x, y - 1),
        (x, y + 1),
        (x + 1, y),
        (x - 1, y),
    ]

    next_set = set([
        (nx, ny)
        for nx, ny in eles
        if -1 < nx < n and -1 < ny < m and maze[nx, ny] == 0
        and isVisitable(nx, ny, n, m, maze)
    ])

    return next_set

def isVisitable(x, y, n, m, maze):
    eles = [
        (x, y - 1),
        (x, y + 1),
        (x - 1, y),
        (x + 1, y)
    ]

    lnk_cnt = sum([
        maze[nx, ny] != 0
        for nx, ny in eles 
        if -1 < nx < n and -1 < ny < m
    ])

    return lnk_cnt == 1 or (((n - 1, m - 1) in eles or (x, y) == (n - 1, m - 1)) and maze[n - 1, m - 1] == 0)

def genMaze(x, y, n, m):
    maze = np.zeros([n, m])
    
    nx, ny = x, y
    maze[nx, ny] = 1

    next_set = set()
    plen = 1
    while True:
        tmp_set = getReachable(nx, ny, n, m, maze);

        if plen > 0 and len(tmp_set) > 0:
            aim_set = tmp_set
            plen = plen - 1
        else:
            plen = 1 << random.randint(1, 7)
            aim_set = next_set.union(tmp_set)

        nx, ny = random.sample(aim_set, 1)[0]

        if isVisitable(nx, ny, n, m, maze):
            maze[nx, ny] = 1 << random.randint(1, 10) / 8

            #os.system('clear')
            #printMaze(n, m, maze, ('  ', '##'), next_set, tmp_set)
            #print plen, tmp_set
            #time.sleep(0.01)

        next_set = next_set.union(aim_set)
        next_set.discard((nx, ny))

        if len(next_set) == 0:
            break


    return maze

def printMaze(n, m, maze, draw_pair, next_set, tmp_set):
    print " " + "_"*m*len(draw_pair[0]) + " "

    s = ""
    for i in range(n):
        s = s + "|"
        for j in range(m):
            if maze[i, j] == 1:
                s = s + draw_pair[0]
            elif maze[i, j] == 2:
                s = s + draw_pair[1]
            else:
                if (i, j) in next_set:
                    s = s + "\x1B[32m" + draw_pair[1] + "\x1B[37m"
                elif (i, j) in tmp_set:
                    s = s + "\x1B[31m" + draw_pair[1] + "\x1B[37m"
                else:
                    s = s + draw_pair[2]

        s = s + "|\n"
    print s + " " + "-"*m*len(draw_pair[0]) + " "


printMaze(10, 20, genMaze(0, 0, 10, 20), ('1', '2', '0'), set(), set())
