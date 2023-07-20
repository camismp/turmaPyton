#Escreva um programa que leia um valor correspondente ao número de jogadores de um time de vôlei.
#O programa deverá ler uma altura para cada um dos jogadores e,ao final,informar a altura média do time.

def Jogadores():
    somaAltura = 0
    numeroJogadores = int(input('Digite o número de jogadores: '))



    for i in range(numeroJogadores):
       altura = float(input('Digite a altura do jogador: '))
       somaAltura += altura

       alturaMedia = somaAltura / numeroJogadores

       print('A altura média do time é: {} '.format(somaAltura / numeroJogadores))
