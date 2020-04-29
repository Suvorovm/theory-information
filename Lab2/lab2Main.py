import string

from Lab1Functions.CalculateEnthropy import *
from Lab1Functions.genrator import *
from Lab1Functions.measure import *
from Lab2.CalculateParameters import calculate_average_length, coef_redundancies
from Lab2.Khartli import calculate_Khartli_code_with_sort
from Lab2.ShennonCod import calculate_Shennon_cod_with_sort

# calculate_Khartli_code_with_sort(probabilityDict)
from Lab2.UniformСode import create_uniform_code_by_dict


def printMenu():
    print("1 - для ввода алфавита\n")
    print("2 - чтобы использовать полный алфовит , вероятности распредленны случайно ()\n")
    print("3  - Закодировать \n")
    print("4  -  Декодировать \n")
    print("5  -  Энтропия источника \n")
    print("6  - Средняя длинна слова\n")
    print("7  - Коэффициент относительной избыточности\n")
    print("8  - Избыточность источника сообщения\n")
    print("9  - Все характиристики\n")


def EnterValues():
    print("Для выходда введите пустую строку\n")
    dic = {}
    while True:
        print("Введите симовл или No, для того, чтобы закончить\n")
        symbl = input()
        if str(symbl).upper() == "NO":
            break
        print("Введите вероятность\n")
        probability = float(input())
        dic[symbl] = probability
    summer = 0
    for key, value in dic.items():
        summer += value
        if summer > 1:
            print("Вероятность > 1. ERROR")
            return None
        return dic


def diplay_result(resultKhartlicod, resultShennoncod, uniformCode):
    print("Кодировка Шеннона \n")
    print_list_probability(resultShennoncod)
    print("Кодировка  Хаффмена \n")
    print_list_probability(resultKhartlicod)
    print("Равномерный код \n")
    print_list_probability(uniformCode)


def verify_message(usrMsg, alphabet):
    for i in usrMsg:
        if i not in alphabet:
            print("Нет нужного символа")
            exit(0)


def encode_msg(usrMsg: str, codingRules: list):
    resultString = ""
    for i in range(0, len(usrMsg)):
        val = [j for j in codingRules if j.symbol == usrMsg[i]][0]
        resultString += val.code
    return resultString


def decode_msg(usrMsg: str, codingRules: list):
    index = 0
    resultString = ""
    while True:
        listVal = [i for i in codingRules if usrMsg.find(i.code, index) == index]
        if len(listVal) == 0:
            return None
        resultString += listVal[0].symbol
        index += len(listVal[0].code)
        if index == len(usrMsg):
            break
    return resultString


def main():
    fullAlphabet = string.ascii_letters + string.digits + ' '
    resultShennoncod = None
    resultKhartlicod = None
    resultUniformCode = None
    enteredAlphabetProbability = None
    currentAlphabet = ""
    while True:
        printMenu()
        userValue = input()
        if userValue == "1":
            enteredAlphabetProbability = EnterValues()
            if enteredAlphabetProbability is None:
                continue
            currentAlphabet = get_alphabet_by_dict(enteredAlphabetProbability)
            resultKhartlicod, resultShennoncod, resultUniformCode = generate_ruls(enteredAlphabetProbability)
        elif userValue == "2":
            enteredAlphabetProbability = generate_probability_dict(fullAlphabet)
            currentAlphabet = fullAlphabet
            resultKhartlicod, resultShennoncod, resultUniformCode = generate_ruls(enteredAlphabetProbability)
        elif userValue == "3":
            print("Введите сообщение для кодирования\n")
            usrMsg = input()
            verify_message(usrMsg, currentAlphabet)
            if resultKhartlicod is None or resultKhartlicod is None:
                print("Кодировка не сгенерирована. Отсутсвют правила")
                continue
            resultMsgKhartlicod = encode_msg(usrMsg, resultKhartlicod)
            resultMsgShennon = encode_msg(usrMsg, resultShennoncod)
            resultMsgUniForm = encode_msg(usrMsg, resultUniformCode)
            print("Код Шеннона = " + resultMsgShennon)
            print("Код Хаффмен = " + resultMsgKhartlicod)
            print("Равномерный код  = " + resultMsgUniForm)
        elif userValue == "4":
            print("\nВведите сообщени\n")
            usrMsg = input()
            print("Использовался Код Шеннона (1)  код Хафмен (2) , Равномерный (3)\n")
            usrChoose = input()
            resultMsg = ""
            if usrChoose == "1":
                resultMsg = decode_msg(usrMsg, resultShennoncod)
            elif usrChoose == "2":
                resultMsg = decode_msg(usrMsg, resultKhartlicod)
            elif usrChoose == "3":
                resultMsg = decode_msg(usrMsg, resultUniformCode)
            if resultMsg is None:
                print("Нельзя декодировать слово. Ошибка")
            else:
                print("\nДекодировано  = " + resultMsg)

        # generate_probability_dict(alphabet)
        elif userValue == "5":
            print("\nВведите строку для определения энтропии (алфавит и вероятности задаются из 1 и 2 пунктов)\n")
            if enteredAlphabetProbability is None:
                print("не заданны вероятности\n")
                continue
            userString = input()
            countInformationShennon = calculate_Shennon_count_information_by_dict(userString,
                                                                                  enteredAlphabetProbability)
            resultEntropy = calculate_entropy(countInformationShennon, userString)
            print("\n\n Энтропия  =  " + str(resultEntropy))
        elif userValue == "6":
            if resultShennoncod is None:
                print("не заданны вероятности или правила\n")
                continue
            avrLengthShennon = calculate_average_length(resultShennoncod)
            avgLengthKhartli = calculate_average_length(resultKhartlicod)
            avgUniformCode = calculate_average_length(resultUniformCode)
            print("Средняя длинна слова Шенона = " + str(avrLengthShennon))
            print("Средняя длинна слова Хафмен = " + str(avgLengthKhartli))
            print("Средняя длинна слова Равномерный код = " + str(avgUniformCode))
        elif userValue == "7":
            if resultShennoncod is None:
                print("не заданны вероятности или правила\n")
                continue
            entropy = calculate_calculate_entropy_by_list(resultShennoncod)
            lengthShennon = calculate_average_length(resultShennoncod)
            avgLengthKhartli = calculate_average_length(resultKhartlicod)
            avgLengthUniformCode = calculate_average_length(resultUniformCode)
            coefKhartli = 1 - entropy / lengthShennon
            coefShennon = 1 - entropy / avgLengthKhartli
            coefUniform = 1 - entropy / avgLengthUniformCode
            print("Коэффициент избыточности по Хаффмен =  " + str(coefKhartli * -1))
            print("Коэффициент избыточности по Шеннону =  " + str(coefShennon * -1))
            print("Коэффициент избыточности для равномерного кода =  " + str(coefUniform))
        elif userValue == "8":
            if resultShennoncod is None:
                print("не заданны вероятности или правила\n")
                continue
            entropyMax = calculate_entropy_by_list_hartli(resultUniformCode)
            entropyShennon = calculate_calculate_entropy_by_list(resultUniformCode)
            overExp = 1 - (entropyShennon / entropyMax)
            print("Избыточность источника сообщения = " + str(overExp))


def generate_ruls(enteredAlphabetProbability):
    resultShennoncod = calculate_Shennon_cod_with_sort(enteredAlphabetProbability)
    resultKhartlicod = calculate_Khartli_code_with_sort(enteredAlphabetProbability)
    resultUniformCode = create_uniform_code_by_dict(enteredAlphabetProbability)
    diplay_result(resultKhartlicod, resultShennoncod, resultUniformCode)
    return resultKhartlicod, resultShennoncod, resultUniformCode


main()
