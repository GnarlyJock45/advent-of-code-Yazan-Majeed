# DAY 10
# PART 1

from collections import deque

with open("input.txt", "r") as file:
    inputString = file.read()


def parser(inputString):
    parts = inputString.split()
    #get the target line
    targetStr= parts[0].strip('[]')

    # we will create a set of the indeces where the light is on
    lights = frozenset(i for i, char in enumerate(targetStr) if char == '#')

    # We will then get the buttons
    buttons = []
    for button in parts[1:-1]:
        button = button.strip('()')
        if button:
            toggles = frozenset(int(x) for x in button.split(','))
            buttons.append(toggles)

    return lights, buttons


def findFewestPresses(lights, buttons):
    # We start with no lights on
    initialState = frozenset()

    # Queue holds: (set_of_currently_on_lights, number_of_presses)
    queue = deque([(initialState, 0)])
    visited = {initialState}

    while queue:
        currentLights, presses = queue.popleft()

        if currentLights == lights:
            return presses

        # Try pressing every button
        for button in buttons:
            nextLights = currentLights ^ button

            if nextLights not in visited:
                visited.add(nextLights)
                queue.append((nextLights, presses + 1))

    return 0


def solveProblem(inputString):
    total = 0
    for line in inputString.strip().split('\n'):
        if line.strip():
            target, buttons = parser(line)
            total += findFewestPresses(target, buttons)
    return total


print(f"Total fewest presses: {solveProblem(inputString)}")
