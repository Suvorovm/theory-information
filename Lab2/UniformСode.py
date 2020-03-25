import math

from Lab1Functions.genrator import create_list_probability_alphabet


def decimal_to_binary(n):
    return bin(n).replace("0b", "")


def create_uniform_code_by_dict(dictProbability):
    listProbability = create_list_probability_alphabet(dictProbability)
    return create_uniform_code(listProbability)


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
