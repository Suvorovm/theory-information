from Lab1Functions.CalculateEnthropy import calculate_calculate_entropy_by_list
from Lab1Functions.measure import *


def calculate_average_length(listProbabilityAlphabet):
    summer = 0
    for i in listProbabilityAlphabet:
        summer += (i.probability * len(i.code))
    return summer


def coefficient_relative_efficiencies(listProbabilityAlphabet):
    return calculate_calculate_entropy_by_list(listProbabilityAlphabet) / calculate_average_length(
        listProbabilityAlphabet)


def coef_redundancies(listProbabilityAlphabet):
    return 1 - coefficient_relative_efficiencies(listProbabilityAlphabet)
