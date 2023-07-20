#08.Escrever um algoritmo que leia 10 números inteiro se,ao final,apresente a soma de todos os
#números lidos;
def soma_inteiros():
    soma = 0 # Valor inicial da variável
    for i in range(10):
        numero = int(input("Digite um número inteiro: "))
        soma += numero

    print("A soma dos números lidos é:", soma)
