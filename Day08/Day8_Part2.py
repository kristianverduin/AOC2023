import math


input = open("input.txt", 'r')
text = input.read()
input.close()

split = text.split('\n')

directions = split[0]
mappings = split[2:(len(split)-1)]
splitMaps = []

for mapping in mappings:
    values = mapping.split(' ')
    node = values[0]
    left = values[2].strip('(,')
    right = values[3].strip(')')
    splitMaps.append((node, left, right))

def findLocation(value):
    for i, map in enumerate(splitMaps):
        if map[0] == value:
            return map, i

def getNext(values, direction):
    location = None
    next = ''
    if direction =='L':
        next, location = findLocation(values[1])
    elif direction == 'R':
        next, location = findLocation(values[2])
    return next, location

def findZ(node):
    current = node
    location = findLocation(node[0])[1]
    directionCounter = 0
    nrSteps = 0

    while not current[0].endswith('Z'):
        current, location = getNext(splitMaps[location], directions[directionCounter])
        nrSteps += 1

        if directionCounter != len(directions)-1:
            directionCounter += 1
        else:
            directionCounter = 0

    return nrSteps

startNodes = []
for map in splitMaps:
    if map[0].endswith('A'):
        startNodes.append(map)

steps = [0] * len(startNodes)

for i, node in enumerate(startNodes):
    steps[i] = findZ(node)

print(math.lcm(*steps))
