#Escreva um algoritmo que calcule a média dos números digitados pelo usuário,se eles forem pares.
# Termine a leitura se o usuário digitar zero(0);
def media():
    soma = 0
    quantidade = 0
    numero = 1
    while numero != 0:
        numero = int(input('Digite um número inteiro: '))
        #verifico se o numero é par ou impar
        if(numero % 2 == 0):
            soma += numero  # soma dos pares
            quantidade += 1 #contador

    if quantidade > 0:
        media = soma / quantidade
        print('A média dos números pares digitados é:', media)

