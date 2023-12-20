import math

input = open("input.txt", 'r')
text = input.read().split('\n')
input.close()

def getDifference(numbs):
    newDiff = []
    for i in range(1, len(numbs)):
        newDiff.append((int(numbs[i]) - int(numbs[i-1])))
    return newDiff

def extrapolateBack(seqs):
    # Method for part 1
    seqs[len(seqs)-1].append(0)
    sum = 0
    
    for i in reversed(range(0, len(seqs)-1)):
        number = seqs[i][len(seqs[i])-1] + seqs[i+1][len(seqs[i+1])-1]
        seqs[i].append(number)
        sum += number

    return seqs, number

def extrapolateForward(seqs):
    # Method for part 2
    seqs[len(seqs)-1].insert(0, 0)
    sum = 0

    for i in reversed(range(0, len(seqs)-1)):
        number = seqs[i][0] - seqs[i+1][0]
        seqs[i].insert(0, number)

    return seqs, number

totalSum = 0
for line in text[0:(len(text)-1)]:
    numbers = line.split(' ')
    difference = [math.inf] * (len(numbers)-1)
    sequences = [[int(i) for i in numbers]]

    while numbers.count(0) != len(numbers):
        numbers = getDifference(numbers)
        sequences.append(numbers)
    
    sequences, sum = extrapolateForward(sequences)
    totalSum += sum

print(totalSum)