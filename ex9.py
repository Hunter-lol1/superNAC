#Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo).

def funcmaiormenor():
    valor = float(input('Digite um valor: '))

    if valor >= 0.0:
        print('O valor digitado é positivo!')
    else:
        print('O valor digitado é negativo!')

funcmaiormenor()