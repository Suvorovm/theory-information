import math


def calculate_entropy(mer, sourceString):
    return mer / len(sourceString)


def calculate_calculate_entropy_by_list(listProbabilityAlphabet):
    summer = 0
    for i in listProbabilityAlphabet:
        summer += i.probability * math.log2(i.probability)
    return -summer


def calculate_entropy_by_list_hartli(listProbabilityAlphabet):
    return math.log2(len(listProbabilityAlphabet))
