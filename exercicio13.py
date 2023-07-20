#Escreva um programa que lido um número, calcule e informe o seu fatorial.
# Ex.:5!=5*4*3*2*1=120.
def fatorial():
    num = 1
    num = int(input('Digite um número inteiro: '))

    if num < 0:
        print('O fatorial não está definido para números negativos')
    elif num == 0:
        print('O fatorial de 0 é 1')
    else:
        fatorial=1
        for i in range(1,num+1):
            fatorial *=i
        print('fatorial é {}'.format(fatorial))
