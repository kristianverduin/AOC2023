
input = open('input.txt', 'r')
text = input.read()
input.close()

lines = text.split('\n')

found = []

def readNumber(line, i, j):
    #Apprently no dupes, check if they have already been found
    if [j, i] not in found:
        found.append([j, i])
    else:
        return 0

    number = line[i]
    while i < len(line)-1 and line[i+1].isdigit():
        i += 1
        number += line[i]

    return int(number)

def moveLeft(line, i):
    while i > 0 and line[i-1].isdigit():
        i -= 1
    return i

def getNumber(line, i, j):
    number = ''
    number2 = 0

    if line[i-1].isdigit() and line[i].isdigit() and line[i+1].isdigit():
        i = moveLeft(line, i)
        number = readNumber(line, i, j)

    elif line[i-1].isdigit() and line[i].isdigit():
        i = moveLeft(line, i)
        number = readNumber(line, i, j)

    elif i < len(line)-1 and line[i].isdigit() and line[i+1].isdigit():
        number = readNumber(line, i, j)

    elif i < len(line)-1 and line[i-1].isdigit() and line[i+1].isdigit():
        number = readNumber(line, i+1, j)
        i = moveLeft(line, i)
        number2 = readNumber(line, i, j)

    elif line[i-1].isdigit():
        i = moveLeft(line, i)
        number = readNumber(line, i, j)

    elif line[i].isdigit():
        number = readNumber(line, i, j)

    elif line[i+1].isdigit():
        number = readNumber(line, i+1, j)

    return number, number2

sum = 0
gearRatios = []

for i in range(len(lines)-1):

    for j in range(len(lines[0])):

        if not lines[i][j].isdigit() and lines[i][j] != '.':
            gearRatio = []

            if j > 0 and lines[i][j-1].isdigit():
                number1, number2 = getNumber(lines[i], j, i)
                sum += number1 + number2
                if number1 != 0:
                    gearRatio.append(number1)
                if number2 != 0:
                    gearRatio.append(number2)

            if j < len(lines[0])-1 and lines[i][j+1].isdigit():
                number1, number2 = getNumber(lines[i], j, i)
                sum += number1 + number2
                if number1 != 0:
                    gearRatio.append(number1)
                if number2 != 0:
                    gearRatio.append(number2)

            if i > 0 and j < len(lines[0])-1 and (lines[i-1][j].isdigit() or lines[i-1][j-1].isdigit() or lines[i-1][j+1].isdigit()):
                number1, number2 = getNumber(lines[i-1], j, i-1)
                sum += number1 + number2
                if number1 != 0:
                    gearRatio.append(number1)
                if number2 != 0:
                    gearRatio.append(number2)
                
            if i < len(lines)-1 and j < len(lines[0]) and (lines[i+1][j].isdigit() or lines[i+1][j-1].isdigit() or lines[i+1][j+1].isdigit()):
                number1, number2 = getNumber(lines[i+1], j, i+1)
                sum += number1 + number2
                if number1 != 0:
                    gearRatio.append(number1)
                if number2 != 0:
                    gearRatio.append(number2)
            
            if len(gearRatio) == 2:
                product = 1
                for z in gearRatio:
                    product *= z
                gearRatios.append(product)

gearSums = 0
for i in gearRatios:
    gearSums += i

print(sum)
print(gearSums)