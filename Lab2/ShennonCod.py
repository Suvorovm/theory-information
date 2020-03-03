import collections
import operator

# probabilityDict упорядоченный словарь с вероятностями
def calculate_Shennon_cod(probabilityDict, resultSum):

    return resultSum


# probabilityDict словарь с вероятностями
def calculate_Shennon_cod_with_sort(probabilityDict):
    resultSum = sum(probabilityDict.values())
    probabilityDict = collections.OrderedDict()
    calculate_Shennon_cod(probabilityDict, resultSum)
