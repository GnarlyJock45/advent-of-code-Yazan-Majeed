# DAY 6 PART 2

with open("input.txt", "r") as file:
    mathHW = file.read()

def toMatrix(str):
    matrix = []
    equations = str.split('\n')
    for equation in equations:
        matrix.append(list(equation))
    return matrix


def solveHW(matrix):
    answer = 0
    blockTotal = 0
    isFirst = True
    op = 43  #the ascii for +

    lengths = [len(r) for r in matrix]
    maxDigits = max(lengths)

    for i in range(maxDigits):
        v = 0
        hasDigit = False

        # read the numgbers form top to bottom
        for r in range(len(matrix) - 1):
            if i < len(matrix[r]):
                charVal = ord(matrix[r][i])
                if charVal != 32:  #32 is the ascii for space character
                    v = v * 10 + (charVal - 48)
                    hasDigit = True
        isEmpty = not hasDigit

        # Check the operator row (the very last row)
        if i < len(matrix[-1]):
            opVal = ord(matrix[-1][i])
            if opVal != 32:
                op = opVal
                isEmpty = False

        if hasDigit:
            if isFirst:
                blockTotal = v
                isFirst = False
            else:
                if op == 43:
                    blockTotal += v
                else:
                    blockTotal *= v

        if isEmpty and not isFirst:
            answer += blockTotal
            blockTotal = 0
            isFirst = True
            op = 43

    if not isFirst:
        answer += blockTotal

    return answer


matrix = toMatrix(mathHW)
print(solveHW(matrix))
