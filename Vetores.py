notas = [] # vetor globla  = Todas as funções podem visualizar e usar este vetor.


def preencherVetor(fim):
    for i in range(fim):
        num = int(input('Informe a {}  nota: '.format (i+1)))
        notas.append(num) #Adicionando notas no vetor

def consultarVetor(fim):
    for i in range (fim):
        print('{}  posição: {}'. format(i+1, notas[i]))

def apagarPosicao(posicao):
    if (len(notas) < posicao):
        print('Impossível remover, pois o tamanho é menor que a posição')
    else:
        del(notas[posicao]) #Excluindo um dado do vetor
        print('Removido com Sucesso!')





