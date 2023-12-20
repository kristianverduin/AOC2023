
def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.split('\n')[:-1]

def calcNrArrangements(springs, groups):
    global cache
    if (springs, tuple(groups)) in cache:
        return cache[(springs, tuple(groups))]
    if springs == '':
        if len(groups) == 0:
            return 1
        else:
            return 0
        
    if len(groups) == 0:
        if '#' in springs:
            return 0
        else:
            return 1
        
    count = 0
    if springs[0] == '.':
        count += calcNrArrangements(springs[1:], groups)

    if springs[0] == '?':
        count += calcNrArrangements('.' + springs[1:], groups)
        count += calcNrArrangements('#' + springs[1:], groups)

    if springs[0] == '#' and len(springs) >= groups[0] and '.' not in springs[0:groups[0]] and (groups[0] == len(springs) or springs[groups[0]] != '#'):
        count += calcNrArrangements(springs[groups[0] + 1:], groups[1:])

    # if springs[0] in '.?':
    #     count += calcNrArrangements(springs[1:], groups)
    
    # if springs[0] in '#?' and groups[0] <= len(springs) and '.' not in springs[0:groups[0]] and (groups[0] == len(springs) or springs[groups[0]] != '#'):
    #     count += calcNrArrangements(springs[groups[0] + 1:], groups[1:])

    cache[(springs, tuple(groups))] = count
    return count

lines = readInput()
total = 0
cache = {}
for line in lines:
    springs = line.split(' ')[0]
    springs = '?'.join([springs] * 5)
    groups = groups = line.split(' ')[1].split(',')
    groups = [int(i) for i in groups] * 5
    total += calcNrArrangements(springs, groups)

print(total)