import random
import string
from random import random

from Lab2.ProbabilityAlphabet import ProbabilityAlphabet


def generate_probability():
    alphabet = string.ascii_letters + string.digits + ' '
    rnd = 100 - len(alphabet)
    probability = []
    sum = 0
    # Рандомно заполняем массив вероятностей
    # и считаем сумму всех элементов

    for i in range(0, len(alphabet)):
        pi = random.randint(1, 1000)
        probability.append(pi)
        sum += pi

    # Делим сумму на каждый элемент
    for i in range(0, len(alphabet)):
        probability[i] = probability[i] / sum

    return probability


def create_dict(alphabet, probability):
    alphabetProbabilityDict = {}
    for i in range(0, len(probability)):
        alphabetProbabilityDict[str(alphabet[i])] = probability[i]
    return alphabetProbabilityDict


def create_list_probability_alphabet(dictAlphabet):
    resultListProbability = []
    for key, value in dictAlphabet.items():
        resultListProbability.append(ProbabilityAlphabet(value, key))
    return resultListProbability


def get_alphabet_by_dict(dictAlphabet):
    alphabet = ''
    for key, value in dictAlphabet.items():
        alphabet += key
    return alphabet


def generate_probability_dict(alphabet):
    localProbability = generate_probability()
    return create_dict(alphabet, localProbability)


def sort_alphabet_list(probabilityList):
    for i in range(0, len(probabilityList)):
        for j in range(0, len(probabilityList)):
            if probabilityList[i].probability > probabilityList[j].probability:
                temp = probabilityList[i]
                probabilityList[i] = probabilityList[j]
                probabilityList[j] = temp


def print_list_probability(probability):
    for i in probability:
        print(i)
