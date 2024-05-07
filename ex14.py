# Ler o nome de 2 times e o número de gols marcados na partida (para cada time). Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.
def times():
    time_a = input('Digite o nome do primeiro time: ')
    time_b = input('Digite o nome do segundo time: ')
    gols_a = int(input(f'Digite a quantidade de gols marcados pelo {time_a}: '))
    gols_b = int(input(f'Digite a quantidade de gols marcados pelo {time_b}: '))

    if gols_a > gols_b:
        print(f'O time vencedor foi o {time_a}')
    elif gols_b > gols_a:
        print(f'O time vencedor foi o {time_b}')
    else:
        print(f'A partida entre {time_a} e {time_b} foi um empate!')

times()