
def readInput():
    with open("test.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

def transpose(array):
    return list(map(list, zip(*array)))

def toString(array):
    return [''.join([str(x) for x in line]) for line in array]

def rollCycle(lines):
    load = 0
    for line in lines:
        for i in range(len(line)):
            if line[i] == 'O':
                index = i
                distance = 0
                while index > 0 and line[index-1] ==  '.':
                    line[index-1] = 'O'
                    line[index] = '.'
                    distance += 1
                    index -= 1
                load += len(line)-index
    return load, lines

def nextCycle(lines, i):
    if i == 0 or i == 1:
        return transpose(lines)
    elif i == 2 or i == 3:
        return transpose(list(reversed(lines)))
    
def oneCycle(lines):
    load = 0
    loads = []
    for i in range(4):
        load, lines = rollCycle(nextCycle(lines, i))
        loads.append(load)

        if i == 3:
            lines = list(reversed(transpose(list(reversed(transpose(lines))))))

    return loads, lines

lines = readInput()

allLoads = []
count = 1
cache = {}
repeat = 0
loads, lines = oneCycle(lines)
print(loads[0])
