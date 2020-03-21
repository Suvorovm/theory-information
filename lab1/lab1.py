import math
import string

from Lab1Functions.CalculateEnthropy import calculate_entropy
from Lab1Functions.measure import calculate_Shennon_count_information
from Lab1Functions.genrator import generate_probability

alphabet = string.ascii_letters + string.digits + ' '
probability = generate_probability()

sourceString = input("Input your message: ")

if sourceString == len(sourceString) * sourceString[0]:
    print("Алфавит состоит из одного символа? y/n")
    if input() == 'y':
        Khartli = len(sourceString) * math.log2(1)
        print("Khartli = ", Khartli)
        print("Энтропия равновероятных событий  = " + str(Khartli / len(sourceString)))
        exit()

Khartli = len(sourceString) * math.log2(len(alphabet))
print("Khartli = ", Khartli)
Shennon = calculate_Shennon_count_information(sourceString, probability)
print("Shennon = ", Shennon)

print("Энтропия равновероятных событий  = " + str(calculate_entropy(Khartli, sourceString)))
print("Энтропия не равновероятных событий  = " + str(calculate_entropy(Shennon, sourceString)))
red = 1 - Shennon / Khartli
if len(sourceString) == 1:
    print("Избыточность не равновероятного источника сообщений = " + "0")
    print("Избыточность  равновероятного источника сообщений = " + "0")
print("Избыточность не равновероятного источника сообщений = " + str(red))
print("Избыточность  равновероятного источника сообщений = " + "0")
