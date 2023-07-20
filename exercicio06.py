#6. Faça um algoritmo que escreva na tela os números de um número inicial a um número final.
# os numeros incial e final devem ser informados pelo usuário;
def escrever_numeros(inicio, fim):
    if(inicio > fim):
        for i in range(inicio,fim-1,-1):
            print(i)
    else:
        for i in range(inicio,fim+1):
            print(i)
