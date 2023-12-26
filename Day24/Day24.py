
def checkBounds(points, min, max):
    return points[0] <= max and points[0] >= min and points[1] <= max and points[1] >= min

def checkPast(x1, x2, y1, y2, px, py):
    if x1 > x2:
        if px > x1 or px > x2:
            return True
    else:
        if px < x1 or px < x2:
            return True
    if y1 > y2:
        if py > y1 or py > y2:
            return True
    else:
        if py < y1 or py < y2:
            return True
    return False

def checkIntersectionPoints(path1, path2):
    (x1, y1), (x2, y2), (x3, y3), (x4, y4) = path1[0], path1[1], path2[0], path2[1]
    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    
    if denominator == 0:
        return None
    
    px = ((((x1*y2) - (y1*x2)) * (x3 - x4)) - ((x1 - x2) * ((x3*y4) - (y3*x4)))) / denominator
    py = ((((x1*y2) - (y1*x2)) * (y3 - y4)) - ((y1 - y2) * ((x3*y4) - (y3*x4)))) / denominator

    if checkPast(x1, x2, y1, y2, px, py) or checkPast(x3, x4, y3, y4, px, py):
        return None
    
    return px, py

def getIntersection(hailstone1, hailstone2, minPos, maxPos):
    position1, velocity1 = hailstone1.split('@')
    position2, velocity2 = hailstone2.split('@')
    x1, y1, z1 = [int(x) for x in position1.split(', ')]
    vx1, vy1, vz1 = [int(x) for x in velocity1.split(', ')]
    x2, y2, z2 = [int(x) for x in position2.split(', ')]
    vx2, vy2, vz2 = [int(x) for x in velocity2.split(', ')]
    newX1, newY1, newX2, newY2 = x1+vx1, y1+vy1, x2+vx2, y2+vy2
    intersectionPoints = checkIntersectionPoints([(x1, y1), (newX1, newY1)], [(x2, y2), (newX2, newY2)])
    if intersectionPoints and checkBounds(intersectionPoints, minPos, maxPos):
        return True
    return False

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip()

def partOne():
    lines = readInput()
    nrIntersected = 0
    checked = []
    MIN = 200000000000000
    MAX = 400000000000000

    for i, hailstone in enumerate(lines.split('\n')):
        for j, hailstone2 in enumerate(lines.split('\n')):
            if i == j or j in checked:
                continue
            nrIntersected += getIntersection(hailstone, hailstone2, MIN, MAX)
        checked.append(i)

    print(nrIntersected)

partOne()
