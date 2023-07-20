#Faça o mesmo que antes, porém, ao invés de ler 10 números, o programa deverá
# ler e somar números até que o valor digitado seja zero(0).
def somaCriterio():
    soma = 0
    numero = 1

    while(numero != 0): # Enquanto o numero for diferente de zero
        numero = int(input("Digite um número inteiro (digite 0 para sair): ")) #num vai receber o valor inteiro por meio de input
        soma += numero # enquanto o usuario digita, o valor é somado

    print('A soma dos números digitados é: {}'.format(soma))  # retorn (' digite o texto': ', (soma))
