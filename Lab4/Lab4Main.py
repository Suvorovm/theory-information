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
        if indexColumn == i:
            continue
        resultColumn.append(matrix[i][indexColumn])
    return resultColumn


def solve_diff_system(sourceMatrix, probabilitiesMatrix):
    return 0


def main():
    sourceMatrix = create_lambda_matrix()
    matrixToSolve = create_matrix_algebraic(sourceMatrix)
    resultProbability = solve_algebraic_system(matrixToSolve, create_b())
    solve_diff_system(matrixToSolve, create_source_probabilities())
    print(resultProbability)
    print("\n")


main()
