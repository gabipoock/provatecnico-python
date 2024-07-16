#faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse ângulo.

import math
ag = float(input('Escreva o ângulo em graus: ')) #ângulo em graus
ar = math.radians(ag) #ar = ângulo regente


seno = math.sin(ar)
cosseno = math.cos(ar)
tangente = math.tan(ar)

print(f'Seno de {ag} graus: {seno:.2f}')
print(f'Cosseno de {ag} graus: {cosseno:.2f}')
print(f'Tangente de {ag} graus: {tangente:.2f}')