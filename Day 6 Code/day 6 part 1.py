# DAY 6 PART 1

with open("input.txt", "r") as file:
    mathHW = file.read()

def toMatrix(str):
    matrix = []
    equations = str.strip().split('\n')
    for equation in equations:
        if equation[0].isdigit():
            stringRow = equation.split()
            stringInt = [int(char) for char in stringRow]
            matrix.append(stringInt)
        else:
            stringRow = equation.split()
            matrix.append(stringRow)

    return matrix

def solveHW(matrix):
    answer = 0
    i = 0
    for i in range(len(matrix[0])):
        temp = 0
        if matrix[4][i] == '+':
            temp = matrix[0][i] + matrix[1][i] + matrix[2][i] + matrix[3][i]
        elif matrix[4][i] == '*':
            temp = matrix[0][i] * matrix[1][i] * matrix[2][i] * matrix[3][i]
        answer += temp

    return answer

matrix = toMatrix(mathHW)
print(solveHW(matrix))
