import math
import heapq
from collections import defaultdict

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()

    return text.strip().split('\n')

def checkDirection(curr_dr, curr_dc, dr, dc, streak):
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if (dr, dc) != (curr_dr, curr_dc):
        return 1
    if (dr, dc) == (curr_dr, curr_dc):
        return streak + 1
    
def checkDirection2(curr_dr, curr_dc, dr, dc, streak):
    if (dr, dc) == (curr_dr, curr_dc):
        return streak + 1
    if (dr, dc) == (-curr_dr, -curr_dc):
        return None
    if streak >= 4 or (curr_dr, curr_dc) == (0,0):
        return 1


def dijkstra(graph, checkDirection, check):
    distances = {(i, j): defaultdict(lambda: math.inf) for j in range(len(graph[0])) for i in range(len(graph))}
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = [(0, (0, 0), (0, 0), 1)]

    while queue:
        dist, (x, y), (curr_dr, curr_dc), streak = heapq.heappop(queue)

        for dr, dc in directions:
            newStreak = checkDirection(curr_dr, curr_dc, dr, dc, streak)
            nx, ny = x + dr, y + dc

            if not newStreak or newStreak == check:
                continue

            if 0 <= nx < len(graph) and 0 <= ny < len(graph[0]):
                newDist = dist + int(graph[nx][ny])
                if newDist < distances[(nx, ny)][(dr, dc, newStreak)]:
                    distances[(nx, ny)][(dr, dc, newStreak)] = newDist
                    heapq.heappush(queue, (newDist, (nx, ny), (dr, dc), newStreak))

    return distances
            
def partOne(graph):
    distances = dijkstra(graph, checkDirection, 4)
    print(min(distances[(len(graph)-1, len(graph[0])-1)].values()))

def partTwo(graph):
    distances = dijkstra(graph, checkDirection2, 11)
    print(min(heat_loss for (_, _, streak), heat_loss in distances[len(graph) - 1, len(graph[0]) - 1].items() if streak >= 4))

lines = readInput()
partOne(lines)
partTwo(lines)