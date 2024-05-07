#A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

def funcjorn():
    ht_mensal = float(input('Digite a quantidade de horas trabalhadas no mês: '))
    sh = float(input('Digite o valor do salário por hora: '))
    st = float(input('Digite o valor do salário total: '))

    ht_semanal = ht_mensal / 4
    

    if ht_semanal > 40:
        ht_extra = (ht_semanal -40) * 4 * sh + st
        print(f'O seu salário será de: {ht_extra}')
    else:
        print(f'O seu salário será de: {st}')

funcjorn()