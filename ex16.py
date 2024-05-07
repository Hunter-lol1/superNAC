#)Uma empresa quer verificar se um empregado está qualificado para a aposentadoria ou não. Para estar em condições, um dos seguintes requisitos deve ser satisfeito: - Ter no mínimo 65 anos de idade. - Ter trabalhado no mínimo 30 anos. - Ter no mínimo 60 anos e ter trabalhado no mínimo 35 anos. Com base nas informações acima, faça um algoritmo que leia: o número do empregado (código), o ano de seu nascimento e o ano de seu ingresso na empresa. O programa deverá escrever a idade e o tempo de trabalho do empregado e a mensagem 'Requerer aposentadoria' ou 'Não requerer'.

def funcaposentadoria(codigo, ano_nascimento, ano_entrada):
    idade = 2024 - ano_nascimento
    tempo_trabalho = 2024 - ano_entrada

    if idade >= 65 or tempo_trabalho >= 30 or idade >= 60 and tempo_trabalho >= 35:
        print(f'Empregado {matricula}: nascido em {ano_nascimento} e ingressado no ano de {ano_entrada}')
        print(f'Com {idade} anos e {tempo_trabalho} anos trabalhados')
        print('Deverá requerer aposentadoria')
    else: 
        print(f'Empregado {matricula}: nascido em {ano_nascimento} e ingressado no ano de {ano_entrada}')
        print(f'Com {idade} anos e {tempo_trabalho} anos trabalhados')
        print('Não deverá requerer aposentadoria')

matricula = int(input('Digite a matrícula do empregado: '))
nasc = int(input('Digite o nascimento do empregado: '))
entrada = int(input('Digite o ano de entrada do empregado na empresa: '))

funcaposentadoria(matricula, nasc, entrada)