#Um posto está vendendo combustíveis com a seguinte tabela de descontos: Escreva um algoritmo que leia o número de litros vendidos e o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 4,89 e o preço do itro do álcool é R$ 3,39.

def funcposto():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        a = 3.39
        g = 4.89
        if opcao_escolhida == 1:
            litros_comprados = float(input('Digite a quantidade em litros de álcool que deseja comprar: '))
            valor = a * litros_comprados
            print(f'O total da compra é de R$ {valor}')
        elif opcao_escolhida == 2:
            litros_comprados = float(input('Digite a quantidade em litros de gasolina que deseja comprar: '))
            valor = g * litros_comprados
            print(f'O total da compra é de R$ {valor}')
        else:
            print('Opção invalida, tente novamente!')
    except: print('Opção invalida, tente novamente!')

funcposto()