from Lab1Functions.genrator import *
from Lab2.ProbabilityAlphabetKhartli import ProbabilityAlphabetKhartli


# listProbability - список ProbabilityAlphabetKhartli 's. производисят сворачивание
def roll_up_Khartli_recursively(listProbability):
    if len(listProbability) == 1:
        return listProbability
    sort_alphabet_list(listProbability)
    downElement = listProbability[len(listProbability) - 1]
    upperElement = listProbability[len(listProbability) - 2]
    resultElement = ProbabilityAlphabetKhartli(downElement, upperElement, True)
    newList = listProbability[:len(listProbability) - 2]
    newList.append(resultElement)
    return roll_up_Khartli_recursively(newList)


# probabilityAlphabetKhartliNode - текущее звено . resultList - результирующий лист. Разварот списка
def get_result_list(probabilityAlphabetKhartliNode: ProbabilityAlphabetKhartli, resultList: list, offset, spaceCount):
    offset += spaceCount
    rightSide = probabilityAlphabetKhartliNode.RightSide
    leftSide = probabilityAlphabetKhartliNode.LeftSide
    if leftSide is None and rightSide is None:
        print_node(probabilityAlphabetKhartliNode, offset)
        return
    if leftSide is None:
        rightSide.code += "0"
        print(rightSide.code, end="\t")
        return
    if rightSide is None:
        leftSide.code += "1"
        print(leftSide.code, end="\t")
        return
    if not leftSide.TemporaryNode:
        resultList.append(leftSide)
    leftSide.code += probabilityAlphabetKhartliNode.code
    leftSide.code += "1"

    get_result_list(leftSide, resultList, offset, spaceCount)

    print_node(probabilityAlphabetKhartliNode, offset)
    if not rightSide.TemporaryNode:
        resultList.append(rightSide)
    rightSide.code += probabilityAlphabetKhartliNode.code
    rightSide.code += "0"
    get_result_list(rightSide, resultList, offset, spaceCount)


# dictAlphabetDict - словар
def calculate_Khartli_code_with_sort(dictAlphabetProbability):
    probabilityAlphabetList = create_list_probability_alphabet(dictAlphabetProbability)
    print("\n\nКод Хафмена\n\n")
    for i in range(0, len(probabilityAlphabetList)):
        probabilityAlphabetList[i].__class__ = ProbabilityAlphabetKhartli
    rol_up_list = roll_up_Khartli_recursively(probabilityAlphabetList)
    result_list = []
    get_result_list(rol_up_list[0], result_list, 0, 10)
    return result_list


def print_node(node, offset):
    print()
    for i in range(0, offset):
        print(end="\t")

    temp = node.code
    if node.code == "":
        temp = "-"
    print(str(temp) + "[" + str(node.symbol) + "]")
