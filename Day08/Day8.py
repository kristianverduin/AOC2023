
input = open("input.txt", 'r')
text = input.read()
input.close()

split = text.split('\n')

directions = split[0]
mappings = split[2:(len(split)-1)]
splitMaps = []

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
    return next[0], location

for mapping in mappings:
    values = mapping.split(' ')
    node = values[0]
    left = values[2].strip('(,')
    right = values[3].strip(')')
    splitMaps.append((node, left, right))

current = 'AAA'
location = findLocation(current)[1]
directionCounter = 0
nrSteps = 0

while current != 'ZZZ':
    current, location = getNext(splitMaps[location], directions[directionCounter])
    nrSteps += 1

    if directionCounter != len(directions)-1:
        directionCounter += 1
    else:
        directionCounter = 0

print(nrSteps)