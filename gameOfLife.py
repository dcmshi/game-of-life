from graphics import *
import pprint
import random

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
            return 0
        else:
            return 1
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
            square = Rectangle(Point(j*50, i*50), Point(j*50-50, i*50-50))
            if grid[j][i]:
                square.setFill('red')
            else:
                square.setFill('blue')
            square.draw(win)

def main():
    dimX, dimY = [5, 5]
    win = GraphWin('Conways Game of Life', width = dimX * 50, height = dimY * 50)
    grid = makeGrid(5,5)
    pp.pprint(grid)
    while True:
        grid = getNextGrid(grid, dimX, dimY)
        drawGrid(grid, dimX, dimY, win)
        pp.pprint(grid)
    win.close()

main()
