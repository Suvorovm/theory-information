from random import random

import random
import string
import math

alphabet = string.ascii_letters + string.digits + ' '

# count = int(input("Количество символов в сообщении"))
# randomString = ''.join([random.choice(string.ascii_letters + string.digits + ' ') for n in range (0, count)])
# print("Сгенерированное сообщение:")
# print(randomString)
rnd = 100 - len(alphabet)
probability = []
sum = 0
# Рандомно заполняем массив вероятностей
# и считаем сумму всех элементов


for i in range(0, len(alphabet)):
    pi = random.randint(1, 1000)
    probability.append(pi)
    sum += pi
probability.append(rnd)
sum += rnd

for i in range(0, len(alphabet)):
    print(probability[i])

# Делим сумму на каждый элемент
for i in range(0, len(alphabet)):
    probability[i] = probability[i] / sum
    print(probability[i])

str1 = input("Input your message: ")

if(str1 == len(str1)*str1[0]):
        print("Алфавит состоит из одного символа? y/n")
        if(input() == 'y'):
            Khartli = len(str1) * math.log2(1)
            print("Khartli = ", Khartli)
            print("Энтропия равновероятных событий  = " + str(Khartli / len(str1)))
            exit()


Khartli = len(str1) * math.log2(len(alphabet))
print("Khartli = ", Khartli)
Shennon = 0
for i in range(0, len(str1)):
    for j in range(0, len(alphabet)):
        if (str1[i] == alphabet[j]):
            Shennon += probability[j] * math.log2(probability[j])
            #print(i, ":Shennon = ", Shennon)
            break
Shennon *= -1
print("Shennon = ", Shennon)



print("Энтропия равновероятных событий  = " + str(Khartli / len(str1)))
print("Энтропия не равновероятных событий  = " + str(Shennon / len(str1)))
red = ((Khartli - Shennon)/Shennon)/len(alphabet)
if len(str1) == 1:
    print("Избыточность не равновероятного источника сообщений = " + "0")
    print("Избыточность  равновероятного источника сообщений = " + "0")
print("Избыточность не равновероятного источника сообщений = " + str(red) )
print("Избыточность  равновероятного источника сообщений = " + "0" )