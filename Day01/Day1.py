import os
import math

input = open("input.txt", "r")
text = input.read()
input.close()

def partOne():
    sum = 0
    numbers = ''

    for i in text:
        if i.isdigit():
            numbers += i
        if i == '\n':
            number = numbers[0] + numbers[len(numbers)-1]
            sum += int(number)
            numbers = ''

    print(sum)

def findAll(string, query):
    answer = []
    for i in range(len(string) - len(query) + 1):
        if string[i:].startswith(query):
            answer.append(i)
    return answer

def partTwo():

    numberDict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    values = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    lines = text.split('\n')
    sum = 0

    for line in lines:
        if line == '':
            continue
        minIndex = math.inf
        min = math.inf
        maxIndex = -math.inf
        max = -math.inf
        for i in values:
            indices = findAll(line, i)
            for index in indices:
                if index > -1 and index < minIndex:
                    minIndex = index
                    if i.isdigit():
                        min = i
                    else:
                        min = numberDict[i]
                if index > -1 and index > maxIndex:
                    test = index
                    maxIndex = index
                    if i.isdigit():
                        max = i
                    else: 
                        max = numberDict[i]
        total = min + max
        sum += int(total)

    print(sum)

partOne()
partTwo()