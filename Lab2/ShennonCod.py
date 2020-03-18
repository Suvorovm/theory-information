
from Lab1Functions.genrator import *


def calculate_Shennon_cod(probabilityList, resultSum, leftBoard, rightBoard):
    summerLeft = 0
    summerRight = 0
    index = 0
    if rightBoard - leftBoard == 1:
        return
    for i in range(leftBoard, rightBoard):
        summerLeft += probabilityList[i].probability
        if summerLeft >= resultSum / 2:
            probabilityList[i].code += "0"
            index = i
            break
        probabilityList[i].code += "0"

    for i in range(index + 1, rightBoard):
        summerRight += probabilityList[i].probability
        probabilityList[i].code += "1"
    print("\n\n\n----\n")
    print_list_probability(probabilityList)
    print("\n\n\n\n\n")
    calculate_Shennon_cod(probabilityList, summerLeft, leftBoard, index + 1)
    calculate_Shennon_cod(probabilityList, summerRight, index + 1, rightBoard)


# probabilityDict словарь с вероятностями
def calculate_Shennon_cod_with_sort(probabilityDict):
    resultSum = sum(probabilityDict.values())
    probabilityAlphabetList = create_list_probability_alphabet(probabilityDict)
    sort_alphabet_list(probabilityAlphabetList)
    calculate_Shennon_cod(probabilityAlphabetList, resultSum, 0, len(probabilityAlphabetList))
    print_list_probability(probabilityAlphabetList)
