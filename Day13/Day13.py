
def sumArray(array):
    sum = 0
    for numbers in array:
        for number in numbers:
            sum += number
    return sum

def checkHorizontalReflection(pattern, up, down):
    start = up
    smudged = False
    while up >= 0 and down < len(pattern):
        difference = getDifference(pattern[up], pattern[down])
        if difference > 1:
            return False
        if difference == 1:
            smudged = True
        up -= 1
        down += 1
    return start+1, smudged

def getDifference(string1, string2):
    difference = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            difference += 1
    return difference

def findReflection(pattern):
    rows = []
    for i in range(len(pattern)-1):
        difference = getDifference(pattern[i], pattern[i+1])
        if difference <= 1:
            reflectionPoint = checkHorizontalReflection(pattern, i, i+1)
            if reflectionPoint and reflectionPoint[1]:
                rows.append(reflectionPoint[0])
    return rows

def transpose(pattern):
    return list(map(list, zip(*pattern)))

def findReflections(pattern):
    columns = findReflection(transpose(pattern))
    rows = findReflection(pattern)
    return columns, rows

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()

    return text.split('\n\n')

patterns = readInput()
totalCols = []
totalRows = []
for pattern in patterns:
    pattern = pattern.strip().split('\n')
    columns, rows = findReflections(pattern)
    totalCols.append(columns)
    totalRows.append(rows)

nrCols = sumArray(totalCols)
nrRows = sumArray(totalRows)
print(nrCols)
print(nrRows)

print(nrCols + (100 * nrRows))