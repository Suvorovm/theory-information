import math

from Lab1Functions.genrator import create_list_probability_alphabet


def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def create_uniform_code_by_dict(dictProbability):
    print("\n Равномерный код\n")
    listProbability = create_list_probability_alphabet(dictProbability)
    resultList = create_uniform_code(listProbability)
    length = len(listProbability)
    print_uniform(resultList, math.ceil((math.log2(length))))
    return resultList


def create_uniform_code(listProbability: list):
    length = len(listProbability)
    countBit = math.ceil((math.log2(length)))
    for i in range(0, length):
        binForm = decimal_to_binary(i)
        stringBinForm = str(binForm)
        if len(stringBinForm) < countBit:
            stringBinForm = "0" * (countBit - len(stringBinForm)) + stringBinForm
        listProbability[i].code = stringBinForm
    return listProbability


def print_uniform(list, countBits):
    print(" ", end="\t")
    for i in range(0, countBits):
        print(i, end="\t")
    print("\n\n")
    for i in range(0, len(list)):
        print(list[i].symbol, end="\t")
        for j in range(0, len(list[i].code)):
            print(list[i].code[j], end="\t")
        print()
