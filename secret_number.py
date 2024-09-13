# jodo do Número Secreto
from random import randint

print('**************************************')
print('Seja bem vindo ao jogo do Número Secreto!')
print('**************************************')

print('\n')

numero_secreto = randint(1, 101)
numero_escolhido = 0

while True:
    try:
        numero_escolhido = int(input('Escolha um número de 1 a 100: '))
    except:
        print('Você escolheu um número invalido!')
    else:
        if numero_escolhido not in range(1, 101):
            print('Número precisa estar entre 1 a 100!')
            continue
        elif numero_escolhido == numero_secreto:
            print(f"Parabéns! o numero secreto é {numero_secreto}!")

            break
        else:
            print("Você errou!")