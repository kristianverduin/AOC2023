
def readInput():
    with open("input.txt", 'r') as file:
        text = file.read().strip().split('\n\n')
    return text

sections = readInput()
input = [int(x) for x in sections[0].replace("seeds: ", "").split(" ")]
seeds = [(input[i], input[i] + input[i+1]) for i in range(0, len(input), 2)]
maps = [[[int(y) for y in x.split(" ")] for x in sections[i].splitlines()[1::]] for i in range(1, 8)]

def remap(start, end, newSeeds, m):
    for destStart, sourceStart, range in m:
        overlapStart = max(start, sourceStart)
        overlapEnd = min(end, sourceStart + range)

        if overlapStart < overlapEnd:
            newSeeds.append((destStart + (overlapStart - sourceStart), destStart + (overlapEnd - sourceStart)))

            if start < overlapStart:
                seeds.append((start, overlapStart))
            
            if overlapEnd < end:
                seeds.append((overlapEnd, end))

            break
        
    else:
        newSeeds.append((start, end))

for m in maps:
    newSeeds = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        remap(start, end, newSeeds, m)
    seeds = newSeeds

print(min(seeds)[0])