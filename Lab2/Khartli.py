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
def get_result_list(probabilityAlphabetKhartliNode: ProbabilityAlphabetKhartli, resultList: list):
    rightSide = probabilityAlphabetKhartliNode.RightSide
    leftSide = probabilityAlphabetKhartliNode.LeftSide
    if leftSide is None and rightSide is None:
        return
    if leftSide is None:
        rightSide.code += "0"
        return
    if rightSide is None:
        leftSide.code += "1"
        return
    if not leftSide.TemporaryNode:
        resultList.append(leftSide)
    leftSide.code += probabilityAlphabetKhartliNode.code
    leftSide.code += "1"
    get_result_list(leftSide, resultList)
    if not rightSide.TemporaryNode:
        resultList.append(rightSide)
    rightSide.code += probabilityAlphabetKhartliNode.code
    rightSide.code += "0"
    get_result_list(rightSide, resultList)


# dictAlphabetDict - словар
def calculate_Khartli_code_with_sort(dictAlphabetProbability):
    probabilityAlphabetList = create_list_probability_alphabet(dictAlphabetProbability)

    for i in range(0, len(probabilityAlphabetList)):
        probabilityAlphabetList[i].__class__ = ProbabilityAlphabetKhartli
    rol_up_list = roll_up_Khartli_recursively(probabilityAlphabetList)
    result_list = []
    get_result_list(rol_up_list[0], result_list)

