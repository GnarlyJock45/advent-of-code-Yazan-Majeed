# day 12
# part 1

with open("input.txt", "r") as file:
    inputString = file.read()



from tqdm import tqdm
# tqdm so that i dont stare into a blank terminal


def getOrientations(points):
    orientations = []
    # test all combinations of rotating
    for rFlip in (1, -1):
        for cFlip in (1, -1):
            for transpose in (False, True):
                newPts = []
                for r, c in points:
                    nr, nc = r * rFlip, c * cFlip
                    if transpose:
                        nr, nc = nc, nr
                    newPts.append((nr, nc))
                
                # normalize the cords
                minR = min(p[0] for p in newPts)
                minC = min(p[1] for p in newPts)
                normPts = tuple(sorted((p[0] - minR, p[1] - minC) for p in newPts))
                orientations.append(normPts)
                
    return list(set(orientations))


def parser(inputString):
    shapes = {}
    regions = []
    
    lines = inputString.strip().split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
            
        # for the shape definition (: without an x)
        if ':' in line and 'x' not in line:
            idx = int(line.split(':')[0])
            i += 1
            shapeGrid = []
            while i < len(lines) and lines[i].strip() and ':' not in lines[i]:
                shapeGrid.append(lines[i].strip())
                i += 1
                
            points = []
            for r, row in enumerate(shapeGrid):
                for c, char in enumerate(row):
                    if char == '#':
                        points.append((r, c))
                        
            shapes[idx] = {
                'area': len(points),
                'orientations': getOrientations(points)
            }
            
        # for the region requirement (x and :)
        elif 'x' in line and ':' in line:
            parts = line.split(':')
            dim = parts[0].strip()
            width, height = map(int, dim.split('x'))
            counts = list(map(int, parts[1].strip().split()))
            pieceCounts = {idx: counts[idx] for idx in range(len(counts))}
            regions.append((width, height, pieceCounts))
            i += 1
        else:
            i += 1
            
    return shapes, regions


def canFit(width, height, pieceCounts, shapes):
    # check if the area of the shape even fits 
    totalArea = sum(shapes[idx]['area'] * count for idx, count in pieceCounts.items())
    if totalArea > width * height:
        return False
        
    # prrecompute all valid bitmasks for each shape on this specific grid
    shapeMasks = {}
    for idx, count in pieceCounts.items():
        if count > 0:
            masks = []
            for orientation in shapes[idx]['orientations']:
                # slide the piece across every row and column
                for r in range(height):
                    for c in range(width):
                        valid = True
                        mask = 0
                        for dr, dc in orientation:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < height and 0 <= nc < width:
                                mask |= (1 << (nr * width + nc))
                            else:
                                valid = False
                                break
                        if valid:
                            masks.append(mask)
            shapeMasks[idx] = sorted(list(set(masks)))
            if not shapeMasks[idx]: 
                return False
                
    tasks = [(idx, count) for idx, count in pieceCounts.items() if count > 0]
    tasks.sort(key=lambda x: len(shapeMasks[x[0]]))
    
    #we will use depth first search here
    def dfs(taskIdx, countLeft, boardMask, startMaskIdx):
        if taskIdx == len(tasks):
            return True
            
        shapeIdx = tasks[taskIdx][0]
        masks = shapeMasks[shapeIdx]
        
        # try every valid placement for this shape
        for i in range(startMaskIdx, len(masks)):
            m = masks[i]
            if (boardMask & m) == 0: 
                if countLeft == 1:
                    nextCount = tasks[taskIdx+1][1] if taskIdx+1 < len(tasks) else 0
                    if dfs(taskIdx + 1, nextCount, boardMask | m, 0):
                        return True
                else:
                    if dfs(taskIdx, countLeft - 1, boardMask | m, i + 1):
                        return True
        return False
        
    if not tasks: 
        return True
    return dfs(0, tasks[0][1], 0, 0)


def solveProblem(inputString):
    shapes, regions = parser(inputString)
    successfulRegions = 0
    
    for width, height, pieceCounts in tqdm(regions, desc="Packing Presents", unit="region"):
        if canFit(width, height, pieceCounts, shapes):
            successfulRegions += 1
            
    return successfulRegions


print(f"\nTotal regions that fit: {solveProblem(inputString)}")
