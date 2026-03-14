# DAY 10
# PART 2
# this one was a big pain in the a@@ to do 

with open("input.txt", "r") as file:
    inputString = file.read()

import numpy as np
from scipy.optimize import linprog
from tqdm import tqdm


# the parser will return a list of numbers that we can work with 
def parser(inputString):
    parts = inputString.split()
    targetStr = parts[-1].strip('{}')
    targetJoltage = [int(x) for x in targetStr.split(',')]

    buttons = []
    for button in parts[1:-1]:
        button = button.strip('()')
        if button:
            toggles = [int(x) for x in button.split(',')]
            buttons.append(toggles)

    return targetJoltage, buttons


def findFewestPresses(targetJoltage, buttons):
    numCounters = len(targetJoltage)
    numButtons = len(buttons)

    if numButtons == 0:
        return 0

    c = np.ones(numButtons)

    A_eq = np.zeros((numCounters, numButtons))
    for col, button in enumerate(buttons):
        for row in button:
            A_eq[row, col] = 1

    b_eq = np.array(targetJoltage)

    bounds = [(0, None) for _ in range(numButtons)]
    integrality = np.ones(numButtons)

    # we will put our problem in to a system of linear equations to calculate the shortest possible 
    # way to solve the problem. I first tried doing a brute force approach but the code just wouldn't 
    # finish running :/

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, integrality=integrality, method='highs')

    if res.success:
        return int(round(res.fun))
    else:
        return 0 


def solveProblem(inputString):
    total = 0
    
    validLines = [line.strip() for line in inputString.strip().split('\n') if line.strip()]
    
    # i needed to add a loading bar because this was gonna take forever and im impatient
    for line in tqdm(validLines, desc="Configuring Machines", unit="machine"):
        target, buttons = parser(line)
        total += findFewestPresses(target, buttons)
        
    return total


print(f"Total fewest presses: {solveProblem(inputString)}")
