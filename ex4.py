#Para ler 3 números reais e verificar se o primeiro é maior que a soma dos outros dois.

def realmaior():
    N1 = float(input('Digite o primeiro número: '))
    N2 = float(input('Digite o segundo número: '))
    N3 = float(input('Digite o terceiro número: '))
    
    N2N3 = N2 + N3

    if N1 > N2N3:
        print(f'{N1} é maior que a soma do segundo e terceiro número, no caso {N2N3}.')
    else:
        print(f'{N1} náo é maior que a soma do segundo e terceiro número, no caso {N2N3}.')

realmaior()