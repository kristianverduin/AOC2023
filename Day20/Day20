import math

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read()
    return text.strip().split('\n')

def parseInput(input):
    mods = {}
    conjs = {}
    for line in input:
        line = line.split(' -> ')
        if 'broadcaster' in line[0]:
            targets = line[1].split(', ')
            module = {'dest': targets}
            module['type'] = line[0]
            mods[line[0]] = module
        else:
            targets = line[1].split(', ')
            allTargets = []
            for target in targets:
                allTargets.append(target)
            if '%' in line[0]:
                module = {'dest': allTargets}
                module['switch'] = False
            elif '&' in line[0]:
                if line[0][1:] not in conjs:
                    conjs[line[0][1:]] = {}
                module = {'dest': allTargets}
                module['inputs'] = conjs[line[0][1:]]
            module['type'] = line[0][0]
            mods[line[0][1:]] = module
    for conj in conjs:
        for mod in mods:
            if conj in mods[mod]['dest']:
                conjs[conj][mod] = False

    return mods

def allOff(mods):
    for mod in mods.items():
        if mod[1]['type'] == '%':
            if mod[1]['switch'] == True:
                return False
    return True

lines = readInput()
modules = parseInput(lines)

# [lowPulseCount, highPulseCount]
pulseCount = [0, 0]
cycle = 0

while cycle < 1000:
    cycle += 1

    # Pulse to broadcaster and all destinations
    pulseCount[0] += len(modules['broadcaster']['dest']) + 1
    
    queue = [(modules['broadcaster']['dest'], 0, 'broadcaster')]
    while queue:
        dests, pulse, source = queue.pop(0)

        for dest in dests:
            if dest not in modules:
                continue

            if modules[dest]['type'] == '%':
                if pulse == 0:
                    modules[dest]['switch'] = not modules[dest]['switch']
                    pulseType = int(modules[dest]['switch'])
                    pulseCount[pulseType] += len(modules[dest]['dest'])
                    queue.append((modules[dest]['dest'], pulseType, dest))
            elif modules[dest]['type'] == '&':
                modules[dest]['inputs'][source] = pulse
                pulseType = 1 - all(modules[dest]['inputs'].values())
                pulseCount[pulseType] += len(modules[dest]['dest'])
                queue.append((modules[dest]['dest'], pulseType, dest))

    if allOff(modules):
        break

print(((1000//cycle) ** 2) * math.prod(pulseCount))
