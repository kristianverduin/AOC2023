
input = open("input.txt", 'r')
text = input.read()
input.close()

seeds = text.split('\n')[0].split(': ')[1].split(' ')
sections = text.split('\n\n')
locations = []

for seed in seeds:
    current = int(seed)

    for section in sections[1:]:
        existingMap = False
        section = section.split(':')[1].strip('\n').split('\n')

        for line in section:
            end, start, range = line.split(' ')

            if current >= int(start) and current <= (int(start) + int(range)-1):
                current = int(end) + (current-int(start))
                existingMap = True
                break
            
        if not existingMap:
            current = current
    locations.append(current)

print(min(locations))   
