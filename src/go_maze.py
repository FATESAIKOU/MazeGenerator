"""
This is a program to go through a maze provided with the input action text file.

@date: Thu 11/9 14:17:58 CST 2017
@param:
    argv[1] = <maze_file>
    argv[2] = <action_file>
@auther: FATESAIKOU
"""

import sys
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

pprint(loadMap(sys.argv[1]))

