from exercicio04 import somarInteiro
from exercicio05 import tabuada
from exercicio05 import coletarPositivo
from exercicio06 import escrever_numeros
from exercicio07 import impares
from exercicio08 import soma_inteiros
from exercicio09 import somaCriterio
from exercicio10 import media
from exercicio11 import inteiros
from exercicio12 import positivosNegativos
from exercicio13 import fatorial
from exercicio14 import Jogadores
from exercicio15 import miss
from exercicio16 import eleicao
from Vetores import preencherVetor
from Vetores import consultarVetor
from Vetores import apagarPosicao


def montrarMenu():
    print('n\n\nEscolha uma das opções abaixo: ' +
            '\n0. Sair'         +
            '\n1. Execercio 01' +
            '\n2. Execercio 02' +
            '\n3. Execercio 03' +
            '\n4. Execercio 04' +
            '\n5. Execercio 05' +
            '\n6. Execercio 06' +
            '\n7. Execercio 07' +
            '\n8. Execercio 08' +
            '\n9. Execercio 09' +
            '\n10. Execercio 10' +
            '\n11. Execercio 11' +
            '\n12. Execercio 12' +
            '\n13. Execercio 13' +
            '\n14. Execercio 14' +
            '\n15. Execercio 15' +
            '\n16. Execercio 16' +
            '\n17. Execercio 17' +
            '\n18. Execercio 18' +
            '\n19. Execercio 19' +
            '\n20. Execercio 20' +
            '\n21. Preencher Vetor' +
            '\n22. Consultar Vetor' +
            '\n23. Apagar posição Vetor')

def operacao():
    #Chamar o método de cima
    opcao = 1
    while(opcao != 0):
        montrarMenu()
        #Coletar a opção do Usuário
        opcao = int(input('Digite aqui o número da opção escolhida: '))
        #Executo a ação
        if(opcao == 0):
            # Instruções do exercicio 01
            print('Obrigado!')
        elif(opcao == 2):
            return
        elif(opcao == 3):
            return
        elif(opcao == 4):
            # Utilizar o exercício 04
            print('\nExercicio04')
            print(somarInteiro())
        elif(opcao == 5):
            # Exercício 05
            print('\nExercicio05')
            num = int(input('Informe um número: '))
            n = coletarPositivo()
            tabuada(num, n)
        elif(opcao == 6):
            # Exercicio 06
            print('\nExercicio06')
            inicio = int(input('Digite o número inicial: '))
            fim = int(input('Digite o número final: '))
            escrever_numeros(inicio, fim)
        elif(opcao == 7):
            # Exercicio 07
            print('\nExercicio07')
            impares()
        elif(opcao == 8):
            # Exercicio 08
            print('\nExercicio08')
            soma_inteiros()
        elif(opcao == 9):
            # Exercicio 09
            print('\nExercicio09')
            somaCriterio()
        elif(opcao == 10):
            # Exercicio 10
            print('\nExercicio10')
            media()
        elif(opcao == 11):
            # Exercicio 11
            print('\nExercicio11')
            inteiros()
        elif(opcao == 12):
            # Exercicio 12
            print('\nExercicio12')
            positivosNegativos()
        elif(opcao == 13):
            # Exercicio 13
            print('\nExercicio13')
            fatorial()
        elif(opcao == 14):
            print('\nExercicio14')
            Jogadores()
        elif(opcao == 15):
            print('\nExercicio15')
            print(miss())
        elif(opcao == 16):
            print('\nExercicio16')
            print(eleicao())
        elif(opcao == 17):
            return
        elif(opcao == 18):
            return
        elif(opcao == 19):
            return
        elif(opcao == 20):
            return
        elif(opcao == 21):
            num = int(input('Informe o tamanho do vetor: '))
            preencherVetor(num)
        elif(opcao == 22):
            num = int(input('Informe o tamanho do vetor: '))
            consultarVetor(num)
        elif(opcao == 23):
            posicao = int(input('Informe a posição que deseja apagar'))
            apagarPosicao(posicao-1)
        else:
            print('Opção escolhida não é válida escolha novamente!')
