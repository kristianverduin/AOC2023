import copy

# Can be heavily improved -> dictionary? queue/deque? combine seperate methods (probably with dictionary)? find better way than making deep copies?

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip()

def moveEmpty(location, direction):
    if direction == 'left' and location[1] > 0:
            location[1] -= 1
    elif direction == 'right' and location[1] < len(lines[0])-1:
            location[1] += 1
    elif direction == 'down' and location[0] < len(lines)-1:
            location[0] += 1
    elif direction == 'up' and location[0] > 0:
            location[0] -= 1
    else:
        # Beam escaped grid
        return None, None
    return location, direction

def moveMirror(location, direction, currentTile):
    if direction == 'left':
        if currentTile == '/':
            location, direction = moveEmpty(location, 'down')
        else:
            location, direction = moveEmpty(location, 'up')
    elif direction == 'right':
        if currentTile == '/':
            location, direction = moveEmpty(location, 'up')
        else:
            location, direction = moveEmpty(location, 'down')
    elif direction == 'up':
        if currentTile == '/':
            location, direction = moveEmpty(location, 'right')
        else:
            location, direction = moveEmpty(location, 'left')
    elif direction == 'down':
        if currentTile == '/':
            location, direction = moveEmpty(location, 'left')
        else:
            location, direction = moveEmpty(location, 'right')
    return location, direction

def moveSplit(location, direction, currentTile):
    if (direction == 'up' or direction == 'down') and currentTile == '-':
        location2, direction2 = moveEmpty(copy.deepcopy(location), 'left')
        location, direction = moveEmpty(location, 'right')
        if location2:
            locs.append(location2)
            dirs.append(direction2)
    elif (direction == 'right' or direction =='left') and currentTile == '|':
        location2, direction2 = moveEmpty(copy.deepcopy(location), 'down')
        location, direction = moveEmpty(location, 'up')
        if location2:
            locs.append(location2)
            dirs.append(direction2)
    else:
        location, direction = moveEmpty(location, direction)
    return location, direction

def nextLocation(location, direction, currentTile):
    if [location, direction] in seen:
         # Beam already seen
         return None, None
    seen.append([copy.deepcopy(location), direction])
    if currentTile == '.':
            location, direction = moveEmpty(location, direction)
    elif currentTile == '/':
            location, direction = moveMirror(location, direction, currentTile)
    elif currentTile == '\\':
            location, direction = moveMirror(location, direction, currentTile)
    elif currentTile == '|':
            location, direction = moveSplit(location, direction, currentTile)
    elif currentTile == '-':
            location, direction = moveSplit(location, direction, currentTile)
    return location, direction

lines = readInput().split('\n')
locations = []
directions = []
for i in range(len(lines)):
     locations.append([i, 0])
     directions.append('right')
     locations.append([i, len(lines[0])-1])
     directions.append('left')
for i in range(len(lines[0])):
     locations.append([0, i])
     directions.append('down')
     locations.append([len(lines)-1, i])
     directions.append('up')

counts = []

for i in range(len(locations)):
    count = 0
    grid = [['.'for i in range(len(lines[0]))] for j in range(len(lines))]
    seen = []
    locs = [copy.deepcopy(locations[i])]
    dirs = [directions[i]]
    while True:
        if grid[locs[0][0]][locs[0][1]] == '.':
            grid[locs[0][0]][locs[0][1]] = '#'
            count += 1
        locs[0], dirs[0] = nextLocation(locs[0], dirs[0], lines[locs[0][0]][locs[0][1]])
        if locs[0]:
            continue
        elif len(locs) > 1:
            locs = locs[1:]
            dirs = dirs[1:]
        else:
            counts.append(count)
            break

print(max(counts))