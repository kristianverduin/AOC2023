from collections import deque

# Sometimes provides wrong answer due to randomization :/
# Computes the most visited edges and splits them into groups

def group(start, ignore, graph):
    visited = set()
    unvisited = [start]
    while unvisited:
        node = unvisited.pop()
        if node in visited:
            continue
        visited.add(node)
        for connection in graph[node]:
            p = (min(node, connection), max(node, connection))
            if p not in ignore:
                unvisited.append(connection)
    return visited

def countVisits(spans):
    visits = {}
    for span in spans.values():
        for path in span.values():
            start = path[0]
            for node in path[1:]:
                p = (min(start, node), max(start, node))
                if p in visits:
                    visits[p] += 1
                else:
                    visits[p] = 1
                start = node
    return visits

def walkPath(start, graph):
    span = {}
    unvisited = deque([(start, tuple())])
    while unvisited:
        item, path = unvisited.popleft()
        if item in span:
            continue
        path += (item,)
        if len(path) > 1:
            span[item] = path
        for connection in graph[item]:
            unvisited.append((connection, path))
    return span

def getShortestPath(graph):
    # Gets the span for all nodes
    paths = {}
    for node in graph:
        paths[node] = walkPath(node, graph)
    return paths

def initializeGraph(input):
    # Finds all connections between components
    connections = {}
    for line in input:
        component, connected = line.split(': ')
        connected = [x for x in connected.split(' ')]
        for comp in connected:
            connections.setdefault(component, set()).add(comp)
            connections.setdefault(comp, set()).add(component)
    return connections

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

lines = readInput()
connections = initializeGraph(lines)
spans = getShortestPath(connections)
visitCount = countVisits(spans)
sortedVisits = sorted(visitCount.items(), key=lambda x: -x[1])
cuts = set(x[0] for x in sortedVisits[:3])
print("cuts", cuts)
g1 = group(sortedVisits[0][0][0], cuts, connections)
g2 = group(sortedVisits[0][0][1], cuts, connections)
print(len(g1) * len(g2))
