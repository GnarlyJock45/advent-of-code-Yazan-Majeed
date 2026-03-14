# DAY 8
# PART 2

with open("input.txt", "r") as file:
    cords = file.read()


def theBiggerBeautifullerFunction(stringInput):
    coords = []
    for line in stringInput.strip().split('\n'):
        if line.strip():
            coords.append([int(x) for x in line.split(',')])
    n = len(coords)


    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = sum((coords[i][d] - coords[j][d]) ** 2 for d in range(3))
            edges.append((dist_sq, i, j))
    edges.sort()

    # this list will have the ID of all the circuits
    circuitID = list(range(n))
    remainingCircuits = n

    # this loop will keep making connections until only ONE is left
    for dist_sq, box_a, box_b in edges:
        idA = circuitID[box_a]
        idB = circuitID[box_b]


        # If they are in different circuits, connect them
        if idA != idB:
            # Merge circuit B into circuit A by updating the Ids
            for k in range(n):
                if circuitID[k] == idB:
                    circuitID[k] = idA

            remainingCircuits -= 1

            # Check if this connection made them all one big circuit
            if remainingCircuits == 1:
                # Multiply the Xcoordinates
                x1 = coords[box_a][0]
                x2 = coords[box_b][0]
                return x1 * x2


print(theBiggerBeautifullerFunction(cords))
