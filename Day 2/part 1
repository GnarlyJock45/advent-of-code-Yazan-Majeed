import re


# function to check invalid id
def checkInvalidID(id):
    patternForQuestion1 = r"^(\d+)\1$"
    patternForQuestion2 = r"^(\d+)\1+$"
    pattern = re.compile(patternForQuestion2) # this regex pattern will help us find the duplicate patterns in the ids
    if pattern.match(id):
        return True
    else:
        return False

# raw inputs
with open("input.txt", "r") as file:
    inputValues = file.read()

# turn the raw input into lists
inputValues = [[val for val in pair.split('-')] for pair in inputValues.split(',')]


sumOfInvalid = 0

for pair in inputValues:
    for id in range(int(pair[0]), int(pair[1]) + 1):
        if checkInvalidID(str(id)):
            sumOfInvalid += id
        else:
            continue

# final answer:
print(sumOfInvalid)
