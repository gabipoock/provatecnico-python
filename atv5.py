import math

def resolver_equacao_segundo_grau(a, b, c):
    # Calculando o discriminante
    discriminante = b**2 - 4*a*c

    # Verificando o discriminante para determinar o numero de soluções
    if discriminante > 0:
        # Duas soluções reais
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        return 'Duas soluções reais: x1 = {}, x2 = {}.'.format(x1, x2)
    elif discriminante == 0:
        # Uma solução real
        x = -b / (2 * a)
        return 'Uma solução real: x = {}'.format(x)
    else:
        # Nenhuma solução real
        return 'Nenhuma solução real'

# Solicitando ao usuário os coeficientes a, b e c
a = float(input('Digite o coeficiente "a" (diferente de 0): '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))

# Verificando se 'a' é diferente de zero
if a == 0:
    print('O coeficiente "a" deve ser diferente de zero para uma equação de segundo grau.')
else:
    resultado =resolver_equacao_segundo_grau(a, b, c)
    print(resultado)