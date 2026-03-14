# DAY 4 PART 1
# this is the code for day 4 of the advent of code challenge, it is an interesting one (and very challenging)

with open("input.txt", "r") as file:
    inputStr = file.read()

# This function turns the raw string into a list for us to manipulate
def createMatrix(inputStr):
    matrix = [[]]
    rows, cols = 1,1
    for char in inputStr:
        if char == "\n":
            matrix.append([])
            rows += 1
        else:
            matrix[-1].append(char)

    cols = len(matrix[0])
    return matrix, rows, cols

# This function checks individual characters to check if they are a paper roll or not, if so, it adds up the variable
# rollCount which keeps track of the neighboring paper rolls
def checkIfRoll(char, rollCount):
    if char == "@":
        rollCount += 1
        return rollCount
    else:
        return rollCount

# This function checks the neighboring cells for the roll paper and returns if the target roll paper can be accessed
def canAccess(matrix, row, col):
    totalRows = len(matrix)
    totalCols = len(matrix[0])
    neighborRolls = 0

    offsets = [(-1, -1), (-1, 0), (-1, 1),(0, -1), (0, 1),(1, -1), (1, 0), (1, 1)    ]

    for rowOffset, colOffset in offsets:
        neighborRow = row + rowOffset
        neighborCol = col + colOffset
        isRowValid = 0 <= neighborRow < totalRows
        isColValid = 0 <= neighborCol < totalCols

        if isRowValid and isColValid:
            neighborVal = matrix[neighborRow][neighborCol]
            neighborRolls = checkIfRoll(neighborVal, neighborRolls)

    accessible = neighborRolls < 4

    return accessible


matrix, rows, cols = createMatrix(inputStr)

canBeAccessed = 0

for row in range(rows):
    for col in range(cols):
        char = matrix[row][col]
        if char == "@":
            if canAccess(matrix,row,col):
                canBeAccessed += 1


print(f"The number of paper rolls that can be accessed are : {canBeAccessed}")
