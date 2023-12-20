
input = open("input.txt", "r")
text = input.read()
input.close()

games = text.split('\n')
games = games[0:len(games)-1]

def partOne():
    sum = 0
    for game in games:
        impossible = False
        split = game.split(':')
        values = split[1].split(';')
        for value in values:
            if impossible:
                break
            cubes = value.split(',')
            for cube in cubes:
                cube = cube[1:]
                number = cube.split(' ')[0]
                if 'green' in cube:
                    if int(number) > 13:
                        impossible = True
                elif 'red' in cube:
                    if int(number) > 12:
                        impossible = True
                elif 'blue' in cube:
                    if int(number) > 14:
                        impossible = True
        if not impossible:
            sum += int(split[0].split(' ')[1])

    print(sum)

def partTwo():
    sum = 0
    for game in games:
        minRed = 0
        minGreen = 0
        minBlue = 0
        split = game.split(':')
        values = split[1].split(';')
        for value in values:
            cubes = value.split(',')
            for cube in cubes:
                cube = cube[1:]
                number = cube.split(' ')[0]
                if 'green' in cube:
                    if int(number) > minGreen:
                        minGreen = int(number)
                elif 'red' in cube:
                    if int(number) > minRed:
                        minRed = int(number)
                elif 'blue' in cube:
                    if int(number) > minBlue:
                        minBlue = int(number)
        power = minGreen * minRed * minBlue
        sum += power

    print(sum)


partOne()
partTwo()                      