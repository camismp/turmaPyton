#Escreva um algoritmo que leia 20 valores inteiros e ao final exiba:
# A)a soma dos números positivos;
# B)a quantidade de valores negativos;

def positivosNegativos():
    somaPositivos = 0
    quantidadeNegativos = 0

    #loop 20 valores inteiros
    for i in range(1,21):
        num = int(input('Digite um número inteiro: '))

        #verificação de positivos e negativos
        if num > 0:
            somaPositivos += num
        elif num < 0:
            quantidadeNegativos += 1

    print('A soma dos números positivos é:', somaPositivos)
    print('A quantidade de números negativos é:', quantidadeNegativos)

