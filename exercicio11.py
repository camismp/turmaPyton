#Escreva um algoritmo que leia valores inteiros e encontre o maior e o menor deles.
# Termine a leitura se o usuário digitar zero(0);
# Variaveis
def inteiros():
    maior = 0
    menor = 0
    num = 1
    i = 0
    #Digite um número
    # verifique se o número é zero e termine
    while(num != 0):
        num = int(input('Informe um número:'))
        if(num !=0): #enquanto nun for diferente de zero
    #atrubuição de maior e menor
            if(i == 0):
                maior = num
                menor = num
                i = 1
    #verificar se o número é maior
            if num > maior:
                maior = num
    #verificar se o número é menor
            if num < menor:
                menor = num

    print ('maior valor digitado: ', maior)
    print ('menor valor digitado: ', menor)
