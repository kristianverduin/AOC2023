from collections import defaultdict
from collections import deque

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

def partOne():
    lines = readInput()
    start = [(i, j) for i in range(1) for j in range(len(lines[0])) if lines[i][j] == '.']
    end = [(i, j) for i in range(len(lines)-1, len(lines)) for j in range(len(lines[0])) if lines[i][j] == '.']
    print(walk(lines, start, end))

def dfs(graph, start, end):
    distance = 0
    unvisited = deque([(start, 0, {start})])
    
    while unvisited:
        node, currentDistance, visited = unvisited.popleft()
        if node == end:
            distance = max(distance, currentDistance)
            continue
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                newDistance = currentDistance + weight
                newVisited = visited | {neighbor}
                unvisited.append((neighbor, newDistance, newVisited))
    return distance

def findIntersectionDistances(graph, start, intersections):
    distances = {}
    visited = set()
    unvisited = deque([(start, 0)])
    while unvisited:
        (x, y), distance = unvisited.popleft()
        if (x, y) in intersections and (x, y) != start:
            distances[(x, y)] = distance
            continue
        for newX, newY in findNeighbors(graph, x, y):
            if (newX, newY) not in visited:
                visited.add((newX, newY))
                unvisited.append(((newX, newY), distance+1))
    return {start: distances}

def findIntersections(graph):
    intersections = []
    for i in range(len(graph[0])):
        for j in range(len(graph)):
            if graph[i][j] != '#' and len(findNeighbors(graph, i, j)) > 2:
                intersections.append((i, j))
    return intersections

def partTwo():
    lines = readInput()
    start = [(i, j) for i in range(1) for j in range(len(lines[0])) if lines[i][j] == '.']
    end = [(i, j) for i in range(len(lines)-1, len(lines)) for j in range(len(lines[0])) if lines[i][j] == '.']
    intersections = findIntersections(lines)

    nodes = start + intersections + end
    graph = {}
    for node in nodes:
        graph |= findIntersectionDistances(lines, node, nodes)
    print(dfs(graph, start[0], end[0]))

partTwo()