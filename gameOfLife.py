from graphics import *
import pprint
import random
import sys
import time

pp = pprint.PrettyPrinter(indent=2)

canReach = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1]
    ]

def checkNeighbours(grid, x, y, dimX, dimY):
    numLiving = 0
    for move in canReach:
        neighbourX = (x + move[0]) % dimX
        neighbourY = (y + move[1]) % dimY
        if grid[neighbourY][neighbourX] == 1:
            numLiving += 1
    return numLiving

def getNextState(grid, x, y, dimX, dimY):
    curState = grid[y][x]
    numLiving = checkNeighbours(grid, x, y, dimX, dimY)
    if curState == 0:
        if numLiving == 3:
            return 1
        else:
            return 0
    else:
        if 2 <= numLiving <=3:
            return 1
        else:
            return 0

def getNextGrid(grid, dimX, dimY):
    newGrid = []
    for i in range(dimY):
        newRow = []
        for j in range(dimX):
            newRow.append(getNextState(grid, j, i, dimX, dimY))
        newGrid.append(newRow)
    return newGrid

def makeGrid(dimX, dimY):
    grid = []
    for i in range(dimY):
        row = []
        for j in range(dimX):
            row.append(random.randint(0, 1))
        grid.append(row)
    return grid

def drawGrid(grid, dimX, dimY, win):
    for i in range(dimY):
        for j in range(dimX):
            square = Rectangle(Point(j*10+10, i*10+10), Point(j*10, i*10))
            if grid[i][j]:
                square.setFill('white')
            else:
                square.setFill('black')
            square.draw(win)

def main():
    dimX, dimY = [20, 20]
    sleepTime = 5
    args = map(lambda x: int(x), sys.argv[1:])
    
    if len(args) == 2:
        dimX = args[0]
        dimY = args[1]
    elif len(args) == 3:
        dimX = args[0]
        dimY = args[1]
        sleepTime = args[2]
        
    win = GraphWin('Conways Game of Life', width = dimX * 10, height = dimY * 10)
    grid = makeGrid(dimX, dimY)
    
    while True:
        grid = getNextGrid(grid, dimX, dimY)
        drawGrid(grid, dimX, dimY, win)
        time.sleep(sleepTime)
    win.close()

main()
