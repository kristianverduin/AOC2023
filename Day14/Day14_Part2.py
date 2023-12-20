# Potentially combine into one rolling function, lot of repeated code

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

def findChars(lines, char):
    characters = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == char:
                characters.append((i, j))
    return characters

def rollUp(rocks, walls):
    for row, col in sorted(rocks):
        newRow = None

        for potentialNewRow in range(row-1, -1, -1):
            newSpot = potentialNewRow, col
            if newSpot in walls or newSpot in rocks:
                break
            newRow = potentialNewRow
        
        if newRow is not None:
            rocks.remove((row, col))
            rocks.add((newRow, col))

def rollLeft(rocks, walls):
    for row, col in sorted(rocks, key = lambda loc: loc[1]):
        newCol = None

        for potentialNewCol in range(col-1, -1, -1):
            newSpot = row, potentialNewCol
            if newSpot in walls or newSpot in rocks:
                break
            newCol = potentialNewCol
        
        if newCol is not None:
            rocks.remove((row, col))
            rocks.add((row, newCol))

def rollDown(rocks, walls, size):
    for row, col in sorted(rocks, reverse=True):
        newRow = None

        for potentialNewRow in range(row+1, size):
            newSpot = potentialNewRow, col
            if newSpot in walls or newSpot in rocks:
                break
            newRow = potentialNewRow
        
        if newRow is not None:
            rocks.remove((row, col))
            rocks.add((newRow, col))

def rollRight(rocks, walls, size):
    for row, col in sorted(rocks, key=lambda loc: loc[1], reverse=True):
        newCol = None

        for potentialNewCol in range(col+1, size):
            newSpot = row, potentialNewCol
            if newSpot in walls or newSpot in rocks:
                break
            newCol = potentialNewCol
        
        if newCol is not None:
            rocks.remove((row, col))
            rocks.add((row, newCol))

def printGrid(rocks, walls, size):
    print()
    for row in range(size):
        for col in range(size):
            loc = row, col

            print("O" if loc in rocks else ("#" if loc in walls else "."), end="")
        print()

lines = readInput()
rocks = set(findChars(lines, 'O'))
walls = set(findChars(lines, '#'))
size = len(lines)
states: dict[frozenset[tuple[int, int]], int] = {}

i = 0
nrCycles = 1000000000
while i < nrCycles:
    rollUp(rocks, walls)
    rollLeft(rocks, walls)
    rollDown(rocks, walls, size)
    rollRight(rocks, walls, size)

    state = frozenset(rocks)
    if state in states and i < 500:
        distance = nrCycles - i
        loopLength = i - states[state]
        i = nrCycles - distance % loopLength

    states[state] = i
    i += 1

print(sum(size - row for row, _ in rocks))
