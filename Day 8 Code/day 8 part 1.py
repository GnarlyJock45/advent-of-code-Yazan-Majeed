# DAY 8
# PART 1

with open("input.txt", "r") as file:
    cords = file.read()

def TheBigBeautifulFunction(stringInput, num_connections=1000):
    # this block of code will turn the raw string into a workable list
    cords = []
    for line in stringInput.strip().split('\n'):
        if line.strip():
            cords.append([int(x) for x in line.split(',')])
    n = len(cords)

    # the following block will calculate the distances between all the cords
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist_sq = sum((cords[i][d] - cords[j][d]) ** 2 for d in range(3))
            edges.append((dist_sq, i, j))
    edges.sort() # we then sort them

    # we create a list of dictionaries to be used later
    circuits = [{i} for i in range(n)]

    # we will then process the 1000 shortest circuits
    for k in range(min(num_connections, len(edges))):
        _, box_a, box_b = edges[k]
        circuit_a = None
        circuit_b = None
        for circuit in circuits:
            if box_a in circuit:
                circuit_a = circuit
            if box_b in circuit:
                circuit_b = circuit
        # If they are in different circuits then we will merge
        if circuit_a != circuit_b:
            circuits.remove(circuit_a)
            circuits.remove(circuit_b)
            circuits.append(circuit_a.union(circuit_b))

    sizes = [len(circuit) for circuit in circuits]
    sizes.sort(reverse=True)

    # We then multiply the top 3
    if len(sizes) >= 3:
        return sizes[0] * sizes[1] * sizes[2]
    else:
        result = 1
        for s in sizes:
            result *= s
        return result

print(TheBigBeautifulFunction(cords))
