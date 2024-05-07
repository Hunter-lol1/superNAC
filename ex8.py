# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

def funceleitores():
    total_eleitores = int(input('Digite o total de eleitores: '))
    votos_brancos = int(input('Digite o total de votos em branco: '))
    votos_nulos = int(input('Digite o total de votos nulos: '))
    votos_validos = int(input('Digite o total de votos válidos: '))
    if votos_brancos + votos_nulos + votos_validos > total_eleitores:
        print(f'O número de votos é maior que o total de eleitores, tente novamente!')
    else:
        perc_votos_brancos = (votos_brancos / total_eleitores) * 100
        perc_votos_nulos = (votos_nulos / total_eleitores) * 100
        perc_votos_validos = (votos_validos / total_eleitores) * 100

        print(f'O total de eleitores é: {total_eleitores}')
        print(f'O percentual de votos em branco foi: %{perc_votos_brancos}')
        print(f'O percentual de votos nulos foi: %{perc_votos_nulos}')
        print(f'O percentual de votos válidos foi: %{perc_votos_validos}')

funceleitores()