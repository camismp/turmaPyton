#Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos,nulos e válidos.
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

def coletarPositivoInteiro():
    num = int(input())
    while(num <= 0):
        print('Erro!! Informe um positivo:')
        num = int(input('Informe um número:'))
    return num

def transformarPercentual(num, total):
    percentual = (total / num) * 100
    return percentual

def eleicao():
    print('Informe o total de votos brancos: ')
    brancos = coletarPositivoInteiro()
    print('Informe o total de votos nulos: ')
    nulos   = coletarPositivoInteiro()
    print('Informe o total de votos validos: ')
    validos = coletarPositivoInteiro()
    print('Informe o total de votos total ')
    total   = coletarPositivoInteiro()
    #Verificar se o total é igual a brancos, validos e nulos
    if((brancos+nulos+validos) == total):
        pBrancos = transformarPercentual(brancos,total)
        pNulos   = transformarPercentual(nulos, total)
        PValidos = transformarPercentual(validos, total)
        return ' Votos Brancos: {}% \nVotos Nulos: {}% \nVotos Validos: {}%'.format(pBrancos,Pnulos,pValidos)
    else:
        return 'Número de brancos, válidos e nulos é diferente do total de votos, digite novamente'

