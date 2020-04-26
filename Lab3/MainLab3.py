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


def create_p0():
    return numpy.array([0.2, 0.3, 0.4, 0.1])


def create_b():
    return numpy.array([0, 0, 0, 1])


def solve_system(sourceMatrix):
    aMatrix = sourceMatrix.copy()
    aMatrix = aMatrix.transpose()
    for i in range(0, 3):
        for j in range(0, 3):
            if i == j:
                aMatrix[i][j] -= 1
    aMatrix[3] = [1] * 4
    resultX = numpy.linalg.inv(aMatrix).dot(create_b())
    return resultX


def main():
    print(f"P0 = {create_p0()}")
    print("Исхожная матрица")
    matrix = create_matrix()
    print(matrix)
    print("Решение")
    p0 = create_p0()
    pn = p0[:]
    piMatrix = create_matrix()
    for i in range(1, 9):
        piMatrix = matrix.dot(piMatrix)
        print(f"Матрица \n{piMatrix}")
        Pn = p0.dot(piMatrix)
        print(f"P{i}={Pn}")
        print()
    solvedMatrix = solve_system(matrix)

    print(f"\nРешение X =  {solvedMatrix}")


main()
