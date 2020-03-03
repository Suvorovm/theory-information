from random import random

import random
import string


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
    probability.append(rnd)
    sum += rnd

    # Делим сумму на каждый элемент
    for i in range(0, len(alphabet)):
        probability[i] = probability[i] / sum
        print(probability[i])
    return probability


def create_dict(alphabet, probability):
    alphabetProbabilityDict = dict
    for i in range(0, len(probability)):
        alphabetProbabilityDict[alphabet[i]] = probability[i]
    return alphabetProbabilityDict


def generate_probability_dict(alphabet):
    localProbability = generate_probability()
    return create_dict(alphabet, localProbability)
