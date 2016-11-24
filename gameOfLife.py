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
    return numLiving, 8 - numLiving

def getNextState(grid, x, y, dimX, dimY):
    curState = grid[y][x]
    numLiving, numDead = checkNeighbours(grid, x, y, dimX, dimY)
    if curState == 0:
        if numLiving == 3:
            return 0
        return 1
    else:
        if numLiving < 2:
            return 0
        elif 2 <= numLiving <=3:
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


def main():
    dimX, dimY = [5, 5]
    grid = makeGrid(5,5)
    pp.pprint(grid)
    while True:
        grid = getNextGrid(grid, dimX, dimY)
        pp.pprint(grid)

main()
                          


