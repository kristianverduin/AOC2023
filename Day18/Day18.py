import math

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read().strip()
    return text.split('\n')

directionNumMap = {'0': 'R',
                   '1': 'D',
                   '2': 'L',
                   '3': 'U'}

directionMap = {'R': [0, 1],
                'D': [1, 0],
                'L': [0, -1],
                'U': [-1, 0],}

def digDirection(direction, value, digLocations):
    for i in range(value):
        cords = directionMap[direction]
        start = digLocations[len(digLocations)-1]
        current = [start[0]+cords[0], start[1]+cords[1]]
        digLocations.append(current)
    return digLocations

def calcArea(locations):
    # Shoelace formula/algorithm
    area = 0
    for i in range(len(locations)-1):
        area += (locations[i][0] * locations[i+1][1]) - (locations[i][1] * locations[i+1][0])
    area = abs(area) + len(locations)+1
    print(area // 2)

def partOne():
    lines = readInput()
    digLocations = [[0,0]]
    for line in lines:
        direction, value, _ = line.split()
        digDirection(direction, int(value), digLocations)

    calcArea(digLocations)

def partTwo():
    lines = readInput()
    digLocations = [[0,0]]
    for line in lines:
        _,_, instructions = line.split()
        instructions = instructions.strip('()')
        value = int(instructions[1:-1], 16)
        digDirection(directionNumMap[instructions[-1:]], value, digLocations)
    
    calcArea(digLocations)

partTwo()
