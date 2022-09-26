from typing import List
import numpy as np
#[0-9] for Current
#B for blocked

def checkAround():
    pass

def printMaze(maze):
    for e in maze:
        print(e)

def solveDaMaze(maze, pos):
    pass

f = open("maze.mz.txt", "rt")
maze = f.read()
maze = maze.replace(".", "0")
maze = maze.replace("#", "1")
maze = maze.split('\n')
for ligne in maze:
    maze[maze.index(ligne)] = list(ligne)
maze.remove([])
maze = np.array(maze)
print(maze)
#printMaze(maze)