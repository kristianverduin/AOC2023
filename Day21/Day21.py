
def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

def parseMap(input):
    start = (0,0)
    rocks = []
    for i in range(len(input)):
        for j in range(len(input[0])):
            if lines[i][j] == 'S':
                start = (i, j)
            elif lines[i][j] == '#':
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

lines = readInput()
start, rocks = parseMap(lines)
sizeX = len(lines[0])
sizeY = len(lines)

nrSteps = 0
maxSteps = 64
steps = []
steps.append(start)

while nrSteps < maxSteps:
    steps = takeStep(rocks, sizeX, sizeY, steps)
    nrSteps += 1

print(len(steps))
