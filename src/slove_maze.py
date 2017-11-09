"""
This is a program to slove maze-problem.


@date: Thu 11/9 15:39:29 CST 2017
@param:
    argv[1] = <maze_file>
@output:
    action_file
@author: FATESAIKOU
"""

import os
import sys
import time
import copy
import numpy as np

from pprint import pprint
from collections import deque


def loadMap(file_path):
    src = open(file_path, 'r')
    raw_maze = src.read()
    src.close()

    m = raw_maze.index('\n') - 2
    n = raw_maze.count('\n') - 2

    maze = np.zeros([n, m], dtype=np.int)
    for i in xrange(n):
        for j in xrange(m):
            maze[i, j] = int(raw_maze[m + 3 + (m + 3) * i + (j + 1)])

    return maze


def countMaze(maze, froms):
    encode_map = {
        (-1, 0): 'up',
        (1, 0):  'down',
        (0, 1):  'right',
        (0, -1): 'left'
    }

    n, m = maze.shape
    pos = (n - 1, m - 1)

    coin = 0
    actions = []
    while pos != (0, 0):
        if maze[pos] == 2:
            coin += 1
        
        next_pos = tuple(froms[pos])
        actions.append(encode_map[ (pos[0] - next_pos[0], pos[1] - next_pos[1]) ])
        
        pos = next_pos

    return actions, coin


def slove(maze):
    n, m = maze.shape
    froms = np.zeros([n, m, 2], dtype=np.int)
    froms.fill(-1)

    next_que = deque()
    next_que.append([0, 0])
    froms[0, 0] = [0, 0]
    while len(next_que) > 0:
        #os.system('clear')
        #printMaze(maze, froms, ['  ', '--', '##', '=='], next_que)
        #time.sleep(0.01)
        now = next_que.popleft()

        nexts = [
            [now[0] - 1, now[1]],
            [now[0] + 1, now[1]],
            [now[0], now[1] + 1],
            [now[0], now[1] - 1],
        ]

        for i, j in nexts:
            if -1 < i < n and -1 < j < m and maze[i, j] != 0 and list(froms[i, j]) == [-1, -1]:
                next_que.append([i, j])
                froms[i, j] = now

            if i == n - 1 and j == m - 1:
                print "Goal Found!!"
                return countMaze(maze, froms)


def actiondump(actions, output_file):
    src = open(output_file, 'w')

    for a in reversed(actions):
        src.write(a + '\n')
    
    src.close()


def printMaze(maze, froms, draw_pair, path_set):
    n, m = maze.shape

    print " " + "_"*m*len(draw_pair[0]) + " "

    s = ""
    for i in range(n):
        s = s + "|"
        for j in range(m):
            if [i, j] in path_set:
                s = s + "\x1B[32m" + draw_pair[3] + "\x1B[37m"
            elif list(froms[i, j]) != [-1, -1]:
                s = s + "\x1B[31m" + draw_pair[3] + "\x1B[37m"
            elif maze[i, j] == 1:
                s = s + draw_pair[0]
            elif maze[i, j] == 2:
                s = s + draw_pair[1]
            else:
                s = s + draw_pair[2]


        s = s + "|\n"
    print s + " " + "-"*m*len(draw_pair[0]) + " "


maze_file = sys.argv[1]
output_file = sys.argv[2]

maze = loadMap(maze_file)
actions, coin = slove(maze)
actiondump(actions, output_file)
print coin
