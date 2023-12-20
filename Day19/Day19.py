
def readInput():
    with open("input.txt", 'r') as file:
        text = file.read().strip()
    return text.split('\n\n')

def splitInstruction(instruction):
    values = instruction[1].split(':')
    return instruction[0], values[0], values[1]

def readWorkflows(workflow, workflows, values):
    if workflow == 'A':
        return True
    elif workflow == 'R':
        return False
    instructions = workflows[workflow].split(',')
    for instruction in instructions:
        split = ''
        if '<' in instruction:
            split = splitInstruction(instruction.split('<'))
            if values[split[0]] < int(split[1]):
                return readWorkflows(split[2], workflows, values)
        elif '>' in instruction:
            split = splitInstruction(instruction.split('>'))
            if values[split[0]] > int(split[1]):
                return readWorkflows(split[2], workflows, values)
        else:
            return readWorkflows(instruction, workflows, values)

text = readInput()
workflows = text[0]
ratings = text[1]

workflowDict = {}
for workflow in workflows.split('\n'):
    name, workflow = workflow.split('{')
    workflowDict[name] = workflow.strip('}')

result = 0
for rating in ratings.split('\n'):
    valueDict = {}
    values = rating.strip('\{\}').split(',')
    for value in values:
        part, number = value.split('=')
        valueDict[part] = int(number)
    if readWorkflows('in', workflowDict, valueDict):
       result += sum(valueDict.values())

print(result)