import math
import numpy as np

input = open("input.txt", 'r')
text = input.read()
input.close()

tiles = text.split('\n')[:-1]
distance = [[math.inf] * len(tiles[0]) for _ in range(len(tiles))]

def getPipeType(tile):
    pipeType = ''
    match tile:
        case 'S':
            pipeType = 'x'
        case '.':
            pipeType = 'z'
        case 'F':
            pipeType = 'SE'
        case '7':
            pipeType = 'SW'
        case 'J':
            pipeType = 'NW'
        case 'L':
            pipeType = 'NE'
        case '-':
            pipeType = 'EW'
        case '|':
            pipeType = 'NS'

    return pipeType

def updateAdjacentTiles(direction, i, j):
    currentDirection = getPipeType(tiles[i][j])
    #print(currentDirection)
    if i > 0 and distance[i-1][j] == math.inf and 'S' in getPipeType(tiles[i-1][j]) and ('N' in currentDirection or currentDirection == 'x'):
        #Connecting pipe above
        distance[i-1][j] = distance[i][j] + 1
        direction.append('North')
        #print('north')
    elif j > 0 and 'E' in getPipeType(tiles[i][j-1]) and distance[i][j-1] == math.inf and ('W' in currentDirection or currentDirection == 'x'):
        #Connecting pipe left
        distance[i][j-1] = distance[i][j] + 1
        direction.append('West')
        #print('west')
    elif i < len(tiles)-1 and 'N' in getPipeType(tiles[i+1][j]) and distance[i+1][j] == math.inf and ('S' in currentDirection or currentDirection == 'x'):
        #Connecing pipe below
        distance[i+1][j] = distance[i][j] + 1
        direction.append('South')
        #print('south')
    elif j < len(tiles[0]) and 'W' in getPipeType(tiles[i][j+1]) and distance[i][j+1] == math.inf and ('E' in currentDirection or currentDirection == 'x'):
        #Connecing pipe right
        distance[i][j+1] = distance[i][j] + 1
        direction.append('East')
        #print('east')

    return direction

def findStart():
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            if tiles[i][j] == 'S':
                return i, j

currX, currY = findStart()
distance[currX][currY] = 0
directions = []
path = []
path.append([currX, currY])
directions = updateAdjacentTiles(directions, currX, currY)
nextDir = directions.pop()

while True:
    if nextDir == 'South':
        currX = currX+1
    elif nextDir == 'East':
        currY = currY+1
    elif nextDir == 'West':
        currY = currY-1
    elif nextDir == 'North':
        currX = currX-1

    if nextDir == 'x':
        break
    
    path.append([currX, currY])
    directions = updateAdjacentTiles(directions, currX, currY)

    if len(directions) == 0:
        break
    nextDir = directions.pop()

max = -math.inf
for line in distance:
     for i in line:
         if i > max and i != math.inf:
             max = i

max = max + 1
print(max/2)

x, y = findStart()
newPipe = ''
if x > 0 and distance[x-1][y] != math.inf and 'S' in getPipeType(tiles[x-1][y]):
    newPipe += 'N'
if x < len(tiles[0])-1 and distance[x+1][y] != math.inf and 'N' in getPipeType(tiles[x+1][y]):
    newPipe += 'S'
if y > 0 and distance[x][y-1] != math.inf and 'E' in getPipeType(tiles[x][y-1]):
    newPipe += 'W'
if y < len(tiles)-1 and distance[x][y+1] != math.inf and 'W' in getPipeType(tiles[x][y+1]):
    newPipe += 'E'

if 'S' in newPipe and 'N' in newPipe:
    newPipe = '|'
elif 'E' in newPipe and 'W' in newPipe:
    newPipe = '-'
elif 'N' in newPipe and 'E' in newPipe:
    newPipe = 'L'
elif 'N' in newPipe and 'W' in newPipe:
    newPipe = 'J'
elif 'S' in  newPipe and 'W' in newPipe:
    newPipe = '7'
elif 'S' in newPipe and 'E' in newPipe:
    newPipe = 'F'

newTiles = []
for i in range(len(tiles)):
    row = ''
    for j in range(len(tiles[0])):
        if tiles[i][j] == 'S':
            row += newPipe
        else:
            row += tiles[i][j]
    newTiles.append(row)

insideTiles = 0
inside = []
for i in range(len(tiles)):
    isInside = False
    for j in range(len(tiles[0])):
        currentPipe = getPipeType(newTiles[i][j])
        if currentPipe == 'x':
            currentPipe = newPipe
        if 'N' in currentPipe and ([i, j]) in path:
            isInside = not isInside
        if isInside and ([i, j]) not in path:
            insideTiles += 1


print(insideTiles)
