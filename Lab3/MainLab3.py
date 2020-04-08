import numpy as numpy

# 14
N = 14


def c_function():
    return 0.002 * N


def create_matrix():
    p1 = [0.1 + c_function(), 0.2 + c_function(), 0.3 - c_function(), 0.4 - c_function()]
    p2 = [0.2 + c_function(), 0.2 - c_function(), 0.3 + c_function(), 0.3 - c_function()]
    p3 = [0.4 + c_function(), 0.2 + c_function(), 0.1 - c_function(), 0.3 - c_function()]
    p4 = [0.5 + c_function(), 0.2 + c_function(), 0.2 - c_function(), 0.1 - c_function()]
    return numpy.array([p1, p2, p3, p4])


def create_b():
    return numpy.array([0.2, 0.3, 0.4, 0.1])


def solve_system(x, result):
    a = numpy.array([x, x])
    b = numpy.array([result, 1])
    x = numpy.linalg.lstsq(a, b, rcond=None)[0]
    print(x, end="\n")
    return x


def main():
    print("Исхожная матрица")
    matrix = create_matrix()
    p0 = create_b()
    pn = p0
    solvedMatrix = []
    for j in range(0, 4):
        row = solve_system(matrix[j], pn[j])
        solvedMatrix.append(row)
    resultMatrix = solvedMatrix[:]
    solvedMatrix = numpy.array(solvedMatrix)
    resultMatrix = numpy.array(resultMatrix)

    for i in range(1, 8):
        print(f"Матрица", end="\n")
        resultMatrix = numpy.power(solvedMatrix, i)
        print(resultMatrix)
        Pn = p0.dot(resultMatrix)
        print(f"P({i + 1}) = {Pn}")


main()
