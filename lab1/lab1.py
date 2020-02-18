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

# rndBuf = 100
# for i in range(0, len(alphabet)-1):
#    pi = random.uniform(0,rndBuf)
#    probability.append((pi))
#    rndBuf-=pi
# probability.append(rndBuf)

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

str = input("Input your message: ")
Khartli = len(str) * math.log2(len(alphabet))
print("Khartli = ", Khartli)
Shennon = 0
for i in range(0, len(str)):
    for j in range(0, len(alphabet)):
        if (str[i] == alphabet[j]):
            Shennon += probability[j] * math.log2(probability[j])
            print(i, ":Shennon = ", Shennon)
            break
Shennon *= -1
print("Shennon = ", Shennon)


print("Энтропия равновероятных событий  = " + str(Khartli / len(str)))

print("Энтропия не равновероятных событий  = " + str(Shennon / len(str)))