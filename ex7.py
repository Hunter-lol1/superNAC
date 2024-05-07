#Imprimir a tabuada de qualquer número n, informado pelo usuário, no formato 5 x 1 = 5 etc

def functaboada():
    valor = int(input('Digite o número que deseja ver a tabuada: '))
    print('_' * 15)
    print('|{:2} X {:2} = {:3}|'.format(valor, 1, valor*1))
    print('|{:2} X {:2} = {:3}|'.format(valor, 2, valor*2))
    print('|{:2} X {:2} = {:3}|'.format(valor, 3, valor*3))
    print('|{:2} X {:2} = {:3}|'.format(valor, 4, valor*4))
    print('|{:2} X {:2} = {:3}|'.format(valor, 5, valor*5))
    print('|{:2} X {:2} = {:3}|'.format(valor, 6, valor*6))
    print('|{:2} X {:2} = {:3}|'.format(valor, 7, valor*7))
    print('|{:2} X {:2} = {:3}|'.format(valor, 8, valor*8))
    print('|{:2} X {:2} = {:3}|'.format(valor, 9, valor*9))
    print('|{:2} X {:2} = {:3}|'.format(valor, 10, valor*10))
    print('¯' * 15)

functaboada()