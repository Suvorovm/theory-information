import string

from Lab1Functions.genrator import generate_probability_dict, get_alphabet_by_dict, print_list_probability
from Lab2.Khartli import calculate_Khartli_code_with_sort
from Lab2.ShennonCod import calculate_Shennon_cod_with_sort


# calculate_Khartli_code_with_sort(probabilityDict)
def printMenu():
    print("1 - для ввода алфавита\n")
    print("2 - чтобы использовать полный алфовит , вероятности распредленны случайно ()\n")
    print("3  - Закодировать \n")
    print("4  -  Декодировать \n")
    print("5  -  Выйти \n")


def EnterValues():
    print("Для выходда введите пустую строку\n")
    dic = dict
    while True:
        print("Введите симовл\n")
        symbl = input()
        print("Введите вероятность\n")
        probability = float(input())
        dic[symbl] = probability
    summer = 0
    for key, value in dic.items():
        summer += key
    if summer >= 0:
        print("Вероятность > 1. ERROR")
        return None
    return dic


def diplay_result(resultKhartlicod, resultShennoncod, currentAlphabet):
    print("Кодировка Шеннона \n")
    print_list_probability(resultShennoncod)
    print("Кодировка  Хартли \n")
    print_list_probability(resultKhartlicod)


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
            resultKhartlicod, resultShennoncod = generate_ruls(currentAlphabet, enteredAlphabetProbability,
                                                               resultKhartlicod, resultShennoncod)
        elif userValue == "2":
            enteredAlphabetProbability = generate_probability_dict(fullAlphabet)
            currentAlphabet = fullAlphabet
            resultKhartlicod, resultShennoncod = generate_ruls(currentAlphabet, enteredAlphabetProbability,
                                                               resultKhartlicod, resultShennoncod)
        elif userValue == "3":
            print("Введите сообщение для кодирования\n")
            usrMsg = input()
            verify_message(usrMsg, currentAlphabet)
            if resultKhartlicod is None or resultKhartlicod is None:
                print("Кодировка не сгенерирована. Отсутсвют правила")
                continue
            resultMsgKhartlicod = encode_msg(usrMsg, resultKhartlicod)
            resultMsgShennon = encode_msg(usrMsg, resultShennoncod)
            print("Код Шеннона = " + resultMsgShennon)
            print("Код Хартли = " + resultMsgKhartlicod)
        elif userValue == "4":
            print("\nВведите сообщени\n")
            usrMsg = input()
            print("Использовался Код Шеннона (1) или код Хартли (2)\n")
            usrChoose = input()
            resultMsg = ""
            if usrChoose == 1:
                resultMsg = decode_msg(usrMsg, resultShennoncod)
            else:
                resultMsg = decode_msg(usrMsg, resultKhartlicod)
            if resultMsg is None:
                print("Нельзя декодировать слово. Ошибка")
            else:
                print("\nДекодировано  = " + resultMsg)

        # generate_probability_dict(alphabet)


def generate_ruls(currentAlphabet, enteredAlphabetProbability, resultKhartlicod, resultShennoncod):
    resultShennoncod = calculate_Shennon_cod_with_sort(enteredAlphabetProbability)
    resultKhartlicod = calculate_Khartli_code_with_sort(enteredAlphabetProbability)
    diplay_result(resultKhartlicod, resultShennoncod, currentAlphabet)
    return resultKhartlicod, resultShennoncod


main()
