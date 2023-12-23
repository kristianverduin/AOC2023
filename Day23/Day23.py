from collections import defaultdict
import math

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
slopes = "><v^"

def isValid(graph, x, y):
    return 0 <= x < len(graph) and 0 <= y < len(graph[0]) and graph[x][y] != '#'

def findNeighbors(graph, x, y):
    neighbors = []
    for dx, dy in directions:
        newX, newY = dx + x, dy + y
        if isValid(graph, newX, newY):
            neighbors.append((newX, newY))
    return neighbors

def walk(graph, start, end):
    slopeMap = {slope: offset for slope, offset in zip(slopes, directions)}
    unvisited = [(start[0], set())]
    distance = 0
    while unvisited:
        (x, y), visited = unvisited.pop(0)
        if (x, y) == end[0] and len(visited) > distance:
            distance = len(visited)
        elif graph[x][y] in slopes:
            dx, dy = slopeMap[graph[x][y]]
            newX, newY = x + dx, y + dy
            if (newX, newY) not in visited:
                unvisited.append(((newX, newY), visited | {(newX, newY)}))
        else:
            for newX, newY in findNeighbors(graph, x, y):
                if (newX, newY) not in visited:
                    unvisited.append(((newX, newY), visited | {(newX, newY)}))
    return distance

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

lines = readInput()
start = [(i, j) for i in range(1) for j in range(len(lines[0])) if lines[i][j] == '.']
end = [(i, j) for i in range(len(lines)-1, len(lines)) for j in range(len(lines[0])) if lines[i][j] == '.']
print(walk(lines, start, end))