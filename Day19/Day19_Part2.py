import math

def readInput():
    with open("input.txt", 'r') as file:
        text = file.read().strip()
    return text.split('\n\n')

def splitInstruction(instruction):
    values = instruction[1].split(':')
    return instruction[0], values[0], values[1]

def readWorkflows(workflows):
    queue = [{'workflow': 'in', 'x': (1, 4000), 'm': (1, 4000), 'a': (1, 4000), 's': (1, 4000)}]
    total = 0
    while queue:
        current = queue.pop()
        workflow = current['workflow']
        if workflow == 'A':
            total += math.prod(current[i][1] - current[i][0] + 1 for i in 'xmas')
        elif workflow == 'R':
            continue
        else:
            for instruction in workflows[workflow].split(','):
                new = dict(current)
                if '<' in instruction:
                    var, val, target = splitInstruction(instruction.split('<'))
                    new['workflow'] = target
                    new[var] = (new[var][0], int(val)-1)
                    current[var] = (int(val), current[var][1])
                elif '>' in instruction:
                    var, val, target = splitInstruction(instruction.split('>'))
                    new['workflow'] = target
                    new[var] = (int(val)+1, new[var][1])
                    current[var] = (current[var][0], int(val))
                else:
                    new['workflow'] = instruction
                queue.append(new)
    return total

text = readInput()
workflows = text[0]
ratings = text[1]

workflowDict = {}
for workflow in workflows.split('\n'):
    name, workflow = workflow.split('{')
    workflowDict[name] = workflow.strip('}')

print(readWorkflows(workflowDict))