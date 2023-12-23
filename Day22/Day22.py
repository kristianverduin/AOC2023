
def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

def getSortedStack(bricks):
    brickStack = []
    for brick in bricks:
        coords = brick.split('~')
        block = [[int(i) for i in block.split(',')] for block in coords]
        block = sorted(block, key=lambda x: x[2])
        brickStack.append(block)

    brickStack.sort(key=lambda x: x[0][2])
    return brickStack

def getGround(stack):
    maxX = 0
    maxY = 0
    for block1, block2 in stack:
        maxX = max(maxX, block1[0], block2[0])
        maxY = max(maxY, block1[1], block2[1])

    return [[(1, -1) for _ in range(maxX+1)] for _ in range(maxY+1)]

def settleBricks(stack, ground):
    supportedBy = [set() for _ in range(len(stack))]
    supports = [set() for _ in range(len(stack))]

    for i, ((x1, y1, z1), (x2, y2, z2)) in enumerate(stack):

        x1, x2 = sorted((x1, x2))
        y1, y2 = sorted((y1, y2))

        maxHeight = 0
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if ground[y][x][0] > maxHeight:
                    supportedBy[i].clear()
                    maxHeight = ground[y][x][0]

                if ground[y][x][0] == maxHeight and ground[y][x][1] >= 0:
                    supportedBy[i].add(ground[y][x][1])
        for support in supportedBy[i]:
            supports[support].add(i)

        height = z2-z1+1

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                ground[y][x] = (maxHeight+height, i)
        stack[i][0][2] = maxHeight
        stack[i][1][2] = maxHeight+height-1
    return supportedBy, supports

def removableBricks(stack, supportedBy):
    possibleBricks = set(range(len(stack)))
    for brick in supportedBy:
        if len(brick) == 1:
            possibleBricks.discard(brick.pop())
            
    return possibleBricks

def partOne():
    bricks = readInput()
    stack = getSortedStack(bricks)
    ground = getGround(stack)
    supportedBy, supports = settleBricks(stack, ground)
    print(len(removableBricks(stack, supportedBy)))

def checkRemoveChain(stack, supportedBy, supports):
    fallen = 0
    for i in range(len(stack)):
        newStack = ([i])
        falling = set([i])

        while newStack:
            current = newStack.pop(0)

            for supportedByCurrent in supports[current]:
                if len(supportedBy[supportedByCurrent] - falling) == 0:
                    falling.add(supportedByCurrent)
                    newStack.append(supportedByCurrent)

        fallen += len(falling)-1
    return fallen

def partTwo():
    bricks = readInput()
    stack = getSortedStack(bricks)
    ground = getGround(stack)
    supportedBy, supports = settleBricks(stack, ground)
    print(checkRemoveChain(stack, supportedBy, supports))

partOne()
partTwo()
