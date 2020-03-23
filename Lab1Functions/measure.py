import math
import string

alphabet = string.ascii_letters + string.digits + ' '


def calculate_Shennon_count_information(str1, probability):
    Shennon = 0
    for i in range(0, len(probability)):
        Shennon += probability[i] * math.log2(probability[i])

    return Shennon * (- len(str1))


def calculate_Shennon_count_information_by_dict(inputString: str, dictProbability):
    summer = 0
    for key, value in dictProbability.items():
        summer += value * math.log2(value)
    return summer * (- len(inputString))


def calculate_Khartli_(sourceString):
    return len(sourceString) * math.log2(len(alphabet))
