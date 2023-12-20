import numpy as np

input = open('input.txt', 'r')
text = input.read()
input.close()

lines = text.split('\n')

def readNumbers(line):
    numbers = []
    number = ''
    for char in line:
        if char.isdigit():
            number += char
        elif number != '':
            numbers.append(number)
            number = ''
    if number != '':
        numbers.append(number)
    return numbers

def partOne():
    totalCardValue = 0
    for i, line in enumerate(lines):
        if line != '':
            winning, actual = line.split('|')
            winning = winning.split(':')[1]
            winningNumbers = readNumbers(winning)
            actualNumbers = readNumbers(actual)
            cardValue = 0

            for number in actualNumbers:
                if number in winningNumbers:
                    if cardValue == 0:
                        cardValue = 1
                    else:
                        cardValue *= 2
            totalCardValue += cardValue
    print(totalCardValue)

def partTwo():
    totalCardValue = 0
    numberOfCards = np.full(len(lines)-1, 1)
    for i, line in enumerate(lines):
        if line != '':
            winning, actual = line.split('|')
            winning = winning.split(':')[1]
            winningNumbers = readNumbers(winning)
            actualNumbers = readNumbers(actual)
            cardsWon = 0

            for number in actualNumbers:
                if number in winningNumbers:
                    cardsWon += 1
            
            for j in range(numberOfCards[i]):
                index = i+1
                for z in range(cardsWon):
                    numberOfCards[index] += 1
                    index += 1

    print(sum(numberOfCards))
            
partOne()
partTwo()

            
        

        
        