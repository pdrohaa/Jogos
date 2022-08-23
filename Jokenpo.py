from random import randint #Estaremos usando uma função da bilioteca random
import time #Importei a biblioteca time para criar um espaço de tempo entre os prints
opcoes = ('Pedra', 'Papel', 'Tesoura') #Opções de jogada tanto do computado quanto do jogador
cpu = randint(0, 2) #Utilizando o randint pra sortear números entre 0 e 2
print('''Suas opções
[1] PEDRA
[2] PAPEL
[3] TESOURA''') #Aqui estaremos printando as opções que o usuário pode escolher
player = int(input('Qual vai ser sua jogada?')) #Usuário escolhe sua jogada
print('PEDRA')
time.sleep(1)#Usando o sleep para ter um delay de 1 segundo entre os prints
print('PAPEL')
time.sleep(1)
print('TESOOOOOOOOOURA')
time.sleep(1)
print('-='*15) #Apenas visual
print('O computador escolheu {}'.format(opcoes[cpu])) #Aqui ele vai usar o randint para sortear os valores dentro da variável OPCOES para o computador
print('Você jogou {}'.format(opcoes[player])) #Aqui não será sorteado pois o jogador escolheu o número da sua jogada
print('-='*15)

if cpu == 0: #PEDRA
    if player == 0: #Criando condições de vitória ou derrota com as possibilidades que temos.
        print('EMPATE! :|')
    elif player == 1:
        print('VOCE VENCEU!! :D')
    elif player == 2:
        print('COMPUTADOR VENCEU!! :(')
    else:
        print('Jogada Invalida!')    
elif cpu == 1: #PAPEL
    if player == 0:
        print('COMPUTADOR VENCEU!! :(')
    elif player == 1:
        print('EMPATE! :|')
    elif player == 2:
        print('JOGADOR VENCEU! :D')
    else:
        print('Jogada Invalida!')    
elif cpu == 2: #TESOURA
    if player == 0:
        print('JOGADOR VENCEU! :D')
    elif player == 1:
        print('COMPUTADOR VENCEU! :(')
    elif player == 2:
        print('EMPATE! :|')
    else:
        print('Jogada Invalida!')    