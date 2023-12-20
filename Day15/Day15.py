# Rewrite with box class?

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip()

def partOne():
    text = readInput()
    lines = text.split('\n')
    values = []
    for line in lines:
        line = line.split(',')
        for steps in line:
            value = 0
            for char in steps:
                value += ord(char)
                value *= 17
                value = value % 256
            values.append(value)

    print(sum(values))

def partTwo():
    def hash(label):
        value = 0
        for char in label:
            value += ord(char)
            value *= 17
            value = value % 256
        return value

    def removeLens(box, label):
        for i, value in enumerate(boxes[box]):
            if label in value:
                index = i
                while index < len(boxes[box])-1:
                    boxes[box][index] = boxes[box][index+1]
                    index += 1
                if label in value:
                    boxes[box].pop()
                break

    def addLens(box, label, focalLength):
        for i, value in enumerate(boxes[box]):
            if label in value:
                boxes[box][i] = (label, focalLength)
                return
        boxes[box].append((label, focalLength))

    def calcSum():
        sum = 0
        for i, box in enumerate(boxes):
            if len(box) > 0:
                for j, values in enumerate(box):
                    sum += (i+1) * (j+1) * int(values[1])
        return sum
                
    lines = readInput().split('\n')
    boxes = [[] for i in range(256)]
    for line in lines:
        line = line.split(',')
        for steps in line:
            label = ''
            for i, char in enumerate(steps):
                if char == '=':
                    addLens(hash(label), label, steps[i+1])
                    break
                elif char == '-':
                    removeLens(hash(label), label)
                else:
                    label += char
    
    print(calcSum())


partTwo()