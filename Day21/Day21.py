from collections import defaultdict
from collections import deque

# Part 1 takeStep can still be improved a lot.. - Part 1 very slow

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

def parseMap(input):
    start = (0,0)
    rocks = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'S':
                start = (i, j)
            elif input[i][j] == '#':
                rocks.append((i, j))
    return start, rocks

def takeStep(rocks, lenX, lenY, steps):
    newSteps = []
    for step in steps:
        if step[0] > 0 and (step[0]-1, step[1]) not in rocks and (step[0]-1, step[1]) not in newSteps:
            newSteps.append((step[0]-1, step[1]))
        if step[0] < lenX and (step[0]+1, step[1]) not in rocks and (step[0]+1, step[1]) not in newSteps:
            newSteps.append((step[0]+1, step[1]))
        if step[1] > 0 and (step[0], step[1]-1) not in rocks and (step[0], step[1]-1) not in newSteps:
            newSteps.append((step[0], step[1]-1))
        if step[1] < lenY and (step[0], step[1]+1) not in rocks and (step[0], step[1]+1) not in newSteps:
            newSteps.append((step[0], step[1]+1))
    return newSteps

def partOne():
    nrSteps = 0
    maxSteps = 64
    steps = []
    steps.append(start)

    while nrSteps < maxSteps:
        steps = takeStep(rocks, sizeX, sizeY, steps)
        nrSteps += 1

    print(len(steps))

def quadaticForumla(y, n):
    a = (y[2] - (2*y[1]) + y[0]) // 2
    b = y[1] - y[0] - a
    c = y[0]
    return (a*n**2) + (b*n) + c

def possibleMoves(coord, map):
    moves = []
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    for direction in directions:
        newCoord = (coord[0] + direction[0], coord[1] + direction[1])
        if map[newCoord[1] % 131][newCoord[0] % 131] != '#':
            moves.append(newCoord)
    return moves

def bfs(start, map, maxDistance):
    tiles = defaultdict(int)
    visited = set()
    unvisited = deque([(start, 0)])

    while unvisited:
        (x, y), distance = unvisited.popleft()
        if distance == (maxDistance + 1) or (x,y) in visited:
            continue
        tiles[distance] += 1
        visited.add((x, y))

        for step in possibleMoves((x,y), map):
            unvisited.append((step, distance+1))
    return tiles

def calculatePossibleSpots(start, map, maxSteps):
    tiles = bfs(start, map, maxSteps)
    return sum(x for y, x in tiles.items() if y % 2 == maxSteps % 2)

def partTwo():
    cycles = 26501365
    size = len(lines)
    edge = size // 2

    y = [calculatePossibleSpots(start, lines, (edge + i * size)) for i in range(3)]

    print(quadaticForumla(y, ((cycles - edge) // size)))

lines = readInput()
start, rocks = parseMap(lines)
sizeX = len(lines[0])
sizeY = len(lines)

partOne()
partTwo()