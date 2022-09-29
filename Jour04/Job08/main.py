from cgi import test
from typing import List
import numpy as np

""""
To do :
- Create global varaible to store best path number and best path lenght
- backtracking algorithm (only when there is multiple directions to save memory)
- find a path
- backtrack to explore the rest of the maze to make sure this is the best path until there is no more options
- parse the map to replace the best path with X and the rest with .

[2-9] for Current
-1 for blocked
"""

def replace(maze):
    for x in range(len(maze)):
        for y in range(len(maze[x])):
            if maze[x][y] == '.':
                maze[x][y] = 0
            else:
                maze[x][y] = 1


def checkAround(maze, pos, exit):
    way = ""
    if pos[1] + 1 <= exit[1] and maze[pos[0]][pos[1] + 1] == 0:
        way = way + "R"
    if pos[0] + 1 <= exit[0] and maze[pos[0] + 1][pos[1]] == 0:
        way = way + "D"
    if pos[1] - 1 <= 1 and maze[pos[0]][pos[1] - 1] == 0:
        way = way + "L"
    if pos[0] - 1 <= 1 and maze[pos[0] - 1][pos[1]] == 0:
        way = way + "U"
    return way

def printMaze(maze):
    for e in maze:
        print(e)

def solveDaMaze(maze, pos, entrance, exit):

    pass


entrance = [-1, -1]
exit = [-1, -1]
f = open("maze.mz.txt", "rt")
maze = f.read()
maze = maze.split('\n')
for ligne in maze:
    maze[maze.index(ligne)] = list(ligne)
maze.remove([])
replace(maze)
maze = np.array(maze)
entrance, exit = [0, 0], [len(maze) - 1, len(maze[len(maze) - 1]) - 1]
#solveDaMaze(maze, entrance, entrance, exit)
print(maze)
#printMaze(maze)