import math
import string

alphabet = string.ascii_letters + string.digits + ' '


def calculate_Shennon(str1, probability):
    Shennon = 0
    for i in range(0, len(str1)):
        for j in range(0, len(alphabet)):
            if str1[i] == alphabet[j]:
                Shennon += probability[j] * math.log2(probability[j])
                # print(i, ":Shennon = ", Shennon)
                break

    return Shennon


def calculate_Khartli_(sourceString):
    return len(sourceString) * math.log2(len(alphabet))
