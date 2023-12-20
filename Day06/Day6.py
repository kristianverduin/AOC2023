
startingSpeed = 0
speedIncrease = 1
numbers = []

input = open("test.txt", 'r')
text = input.read()
input.close()

lines = text.split('\n')[0:2]

for line in lines:
    values = line.split(':')[1].split()
    numbers.append(values)

time = ''
for i in numbers[0]:
    time += i

distance = ''
for i in numbers[1]:
    distance += i

#totalWaysToWin = 1
# for race in range(len(times)): for part one
#waysToWin = 0

maxTime = int(time)
record = int(distance)
waysToWin = 0

for time in range(maxTime):
    speed = speedIncrease * time
    remainingTime = maxTime - time
    totalDistance = speed * remainingTime
        
    if totalDistance > record:
        waysToWin += 1

#totalWaysToWin *= totalWaysToWin
            
print(waysToWin)
