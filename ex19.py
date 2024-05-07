# Ler 100 valores e escrever quantos desses valores lidos são NEGATIVOS

def funcnegativos():

    count = 0
    for i in range(100):
        valor = float(input('Digite um valor: '))
        if valor < 0:
            count += 1
    print(f'Quantidade de valores negativos: {count}')

funcnegativos()