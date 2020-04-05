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
    print_values(probabilityList, summerLeft, summerRight, leftBoard, rightBoard)
    calculate_Shennon_cod(probabilityList, summerLeft, leftBoard, index + 1)
    calculate_Shennon_cod(probabilityList, summerRight, index + 1, rightBoard)


# probabilityDict словарь с вероятностями
def calculate_Shennon_cod_with_sort(probabilityDict):
    print("\nКод Шеннона\n")
    resultSum = sum(probabilityDict.values())
    probabilityAlphabetList = create_list_probability_alphabet(probabilityDict)
    sort_alphabet_list(probabilityAlphabetList)
    print_header(probabilityAlphabetList)
    calculate_Shennon_cod(probabilityAlphabetList, resultSum, 0, len(probabilityAlphabetList))
    return probabilityAlphabetList


def print_values(listProbability, summerLeft, summerRight, leftBorder, rightBorder):
    for i in range(0, leftBorder):
        print(listProbability[i].code, end="\t\t\t\t")
        #
        # if i == 0 or i == (leftBorder // i):
        #     print("[" + str(summerLeft) + "]", end="")

    for i in range(leftBorder, len(listProbability)):
        print(listProbability[i].code, end="\t\t\t\t")
        # if i == 0:
        #     continue
        # if i == (rightBorder // i):
        #     print("[" + str(summerRight) + "]", end="")

    print()


def print_header(list):
    for i in list:
        print(str(i.symbol) + " {" + str(i.probability) + "}", end="\t")
    print("")
