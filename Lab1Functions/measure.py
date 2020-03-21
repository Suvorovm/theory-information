import math
import string

alphabet = string.ascii_letters + string.digits + ' '


def calculate_Shennon_count_information(str1, probability):
    Shennon = 0
    for i in range(0, len(probability)):
        Shennon += probability[i] * math.log2(probability[i])
        break
    return Shennon * (- len(str1))


def calculate_Khartli_(sourceString):
    return len(sourceString) * math.log2(len(alphabet))
