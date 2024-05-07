#Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

def tresvalores():
    valores = []
    for total in range(3):
        valor = float(input('Digite o valor: '))
        valores.append(valor)
    valores.sort(reverse=True)

    total= valores[0] + valores[1]

    print(f'A soma dos dois maiores valores é de: {total}')

tresvalores()