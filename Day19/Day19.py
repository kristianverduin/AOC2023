
def readInput():
    with open("test.txt", 'r') as file:
        text = file.read().strip()
    return text.split('\n\n')

def splitInstruction(instruction):
    values = instruction[1].split(':')
    return instruction[0], values[0], values[1]

def readWorkflows(workflows, values):
    instructions = workflows['in'].split(',')
    for instruction in instructions:
        split = ''
        if '<' in instruction:
            split = splitInstruction(instruction.split('<'))
        elif '>' in instruction:
            split = splitInstruction(instruction.split('>'))
        else:
            split = instruction
        print(split)

text = readInput()
workflows = text[0]
ratings = text[1]

workflowDict = {}
for workflow in workflows.split('\n'):
    name, workflow = workflow.split('{')
    workflowDict[name] = workflow.strip('}')

for rating in ratings.split('\n'):
    valueDict = {}
    values = rating.strip('\{\}').split(',')
    for value in values:
        part, number = value.split('=')
        valueDict[part] = int(number)
    readWorkflows(workflowDict, valueDict)
    exit()