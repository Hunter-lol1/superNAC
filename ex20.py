#) Faça um algoritmo que receba 6 valores, calcule e mostre a soma de todos eles.

def somavalores():
    valores = []
    for i in range(6):
        valor = float(input('Digite o valor: '))
        valores.append(valor)
    

    total = sum(valores)

    print(f'A soma dos valores é de: {total}')

somavalores()