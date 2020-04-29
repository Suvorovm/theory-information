import numpy as numpy
from scipy.integrate import odeint
import matplotlib
import sympy  as sp

N = 14
t = numpy.linspace(0, 20, 50)  # (0..20) Countitevals = 50


def create_lambda_matrix():
    row1 = [0, 3 + 0.02 * N, 4 + 0.01 * N, 0]
    row2 = [1.5 + 0.03 * N, 0, 0, 2.5 + 0.02 * N]
    row3 = [3.5 + 0.01 * N, 4.5 + 0.02 * N, 0, 0]
    row4 = [0, 5 - 0.02 * N, 4 - 0.03 * N, 0]
    return [row1, row2, row3, row4]


def create_matrix_algebraic(matrix):
    resultTable = []
    for i in range(0, len(matrix)):
        summerIndex = 0
        for j in range(0, len(matrix[0])):
            if i == j:
                continue
            summerIndex += matrix[i][j]
        resultRow = []
        secondPartOfRow = []
        for j in range(0, len(matrix)):
            if i == j:
                continue
            secondPartOfRow.append(-matrix[j][i])
        resultRow.extend(secondPartOfRow)
        resultRow.insert(i, summerIndex)
        resultTable.append(resultRow)
    resultTable[len(resultTable) - 1] = [1] * len(resultTable[0])
    return numpy.array(resultTable)


def create_b():
    return numpy.array([0, 0, 0, 1])


def create_source_probabilities():
    return numpy.array([0.2, 0.25, 0.3, 0.25])


def solve_algebraic_system(sourceMatrix, b):
    return numpy.linalg.solve(sourceMatrix, b)


def get_row_exclude_item(matrix, indexRow, indexExcludedElement):
    resultRow = []
    for i in range(0, len(matrix[indexRow])):
        if indexExcludedElement == i:
            continue
        resultRow.append(matrix[indexRow][i])
    return resultRow


def get_column_excluded_item(matrix, indexColumn, indexExcludedElement):
    resultColumn = []
    for i in range(0, len(matrix)):
        if indexExcludedElement == i:
            continue
        resultColumn.append(matrix[i][indexColumn])
    return resultColumn


def model(p, t):
    difSystem = []
    matrixToSolve = numpy.array(create_lambda_matrix())
    for i in range(0, len(matrixToSolve)):
        row = get_row_exclude_item(matrixToSolve, i, i)
        column = get_column_excluded_item(matrixToSolve, i, i)
        firstTerm = sum(row) * p[i]
        secondTerm = 0
        for j in range(0, len(matrixToSolve[0])):
            if i == j:
                continue
            secondTerm += p[j] * matrixToSolve[j][i]
        difSystem.append(secondTerm - firstTerm)
    return difSystem


def main():
    sourceMatrix = create_lambda_matrix()
    matrixToSolve = create_matrix_algebraic(sourceMatrix)
    resultProbability = solve_algebraic_system(matrixToSolve, create_b())
    print(resultProbability)
    print("\n")
    CountInterval = 15
    deltaT = numpy.linspace(0, 1, CountInterval)
    solved = odeint(model, create_source_probabilities(), deltaT)
    print(solved)


main()
