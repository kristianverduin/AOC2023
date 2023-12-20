import math

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.split('\n')[:-1]

def getEmptyRows(input):
    emptyRows = []
    for i in range(len(input)):
        emptyRow = True
        for j in range(len(input[0])):
            if input[i][j] != '.':
                emptyRow = False
        if emptyRow:
            emptyRows.append(i)
            
    return emptyRows

def getEmptyColumns(input):
    emptyColumns = []
    for j in range(len(input[0])):
        emptyColumn = True
        for i in range(len(input)):
            if input[i][j] != '.':
                emptyColumn = False
        if emptyColumn:
            emptyColumns.append(j)

    return emptyColumns

def expandRows(input):
    skip = False
    i = 0
    while i != len(input):
        if skip == True:
            skip = False
            i += 1
            continue
        emptyRow = True
        for j in range(len(input[0])):
            if input[i][j] != '.':
                emptyRow = False
        if emptyRow == True:
            newRow = '.' * len(input[0])
            input.insert(i, newRow)
            skip = True
        i += 1

    return input

def flipUniverse(input):
    newUniverse = []
    for j in range(len(input[0])):
        newColumn = ''
        for i in range(len(input)):
            newColumn += input[i][j]
        newUniverse.append(newColumn)

    return newUniverse

def findGalaxies(input):
    galaxies = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] != '.':
                galaxies.append([i, j])

    return galaxies

def calcExtra(first, second, emptyRows, emptyColumns):
    extra = 0
    
    if first[0] < second[0]:
        minx, maxx = first[0], second[0]
    else:
        minx, maxx = second[0], first[0]
    for row in emptyRows:
        if minx < row < maxx:
            extra += 1000000 - 1

    if first[1] < second[1]:
        miny, maxy = first[1], second[1]
    else:
        miny, maxy = second[1], first[1]
    for column in emptyColumns:
        if miny < column < maxy:
            extra += 1000000 - 1

    return extra

lines = readInput()
# lines = expandRows(lines)
# flippedUniverse = flipUniverse(lines)
# flippedUniverse = expandRows(flippedUniverse)
galaxies = findGalaxies(lines)
pairs = [(a,b) for i, a in enumerate(galaxies) for b in galaxies[i+1:]]

emptyCols = getEmptyColumns(lines)
emptyRows = getEmptyRows(lines)

shortestPaths = []
for pair in pairs:
    shortest = math.inf
    first = pair[0]
    second = pair[1]
    shortestPaths.append(abs(first[0] - second[0]) + abs(first[1] - second[1]) + calcExtra(first, second, emptyRows, emptyCols))

print(sum(shortestPaths))