#faça um programa que leia o comprimento do cateto oposto,
#cateto adjacente e retornando o valor da hipotenusa.

import math

ca = float(input('Escreva o comprimento do cateto adjacente: '))
co = float(input('Escreva o comprimento do cateto oposto: '))
h = math.hypot(ca,co)
print('O valor da hipotenusa é:',h)