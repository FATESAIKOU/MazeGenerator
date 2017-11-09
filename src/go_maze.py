"""
This is a program to go through a maze provided with the input action text file.

@date: Thu 11/9 14:17:58 CST 2017
@param:
    argv[1] = <maze_file>
    argv[2] = <action_file>
@auther: FATESAIKOU
"""

import os
import sys
import time
import numpy as np

from pprint import pprint

def loadMap(file_path):
    src = open(file_path, 'r')
    raw_maze = src.read()
    src.close()

    m = raw_maze.index('\n') - 2
    n = raw_maze.count('\n') - 2

    maze = np.zeros([n, m])
    for i in xrange(n):
        for j in xrange(m):
            maze[i, j] = int(raw_maze[m + 3 + (n + 3) * i + (j + 1)])

    return maze

def goMaze(maze, action_file):
    action_src = open(action_file, 'r')
    action_map = {
        'up':    lambda p: [p[0] - 1, p[1]],
        'down':  lambda p: [p[0] + 1, p[1]],
        'right': lambda p: [p[0], p[1] + 1],
        'left':  lambda p: [p[0], p[1] - 1]
    }
    
    pos = [0, 0]

    path_set = set()
    path_set.add(tuple(pos))
    while True:
        os.system('clear')
        printMaze(maze, ['  ', '--', '##', 'XD'], path_set)
        time.sleep(0.1)

        action = action_src.readline().rstrip()

        if not action:
            break

        assert action in action_map.keys(), "\x1B[31m[Error]\x1B[37m Undefined Action"
        pos = action_map[action](pos)
        assert maze[tuple(pos)] != 0, "\x1B[31m[Error]\x1B[37m Action: " + action + ", not valid"

        path_set.add(tuple(pos))

    assert (pos[0] - 1, pos[1] - 1) == maze.shape, "\x1B[31m[Error]\x1B[37m " + str(pos) + " is not the goal"


def printMaze(maze, draw_pair, path_set):
    n, m = maze.shape

    print " " + "_"*m*len(draw_pair[0]) + " "

    s = ""
    for i in range(n):
        s = s + "|"
        for j in range(m):
            if (i, j) in path_set:
                s = s + "\x1B[32m" + draw_pair[3] + "\x1B[37m"
            elif maze[i, j] == 1:
                s = s + draw_pair[0]
            elif maze[i, j] == 2:
                s = s + draw_pair[1]
            else:
                s = s + draw_pair[2]


        s = s + "|\n"
    print s + " " + "-"*m*len(draw_pair[0]) + " "

maze = loadMap(sys.argv[1])
goMaze(maze, sys.argv[2])

