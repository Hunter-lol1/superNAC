#Calcular a média final dadas as notas das 3 provas e produzir uma saída com a média e a situação do aluno de acordo com o seguinte critério: média >= 6, aprovado; média >=3 e média < 6, recuperação; média < 3, reprovado. Considerar também o número de faltas do aluno: se forem mais que 15 faltas, o aluno estará automaticamente reprovado (o usuário deve fornecer o número de faltas). Se o aluno se encontrar em recuperação, solicitar a nota da quarta prova e, após calcular a média final, informar se o aluno passou (média final >=5) ou não.

def aprovacao():
    
    faltas = int(input('Digite a quantidade de faltas do aluno: '))
    prova1 = float(input('Digite a nota da primeira prova: '))
    prova2 = float(input('Digite a nota da segunda prova: '))
    prova3 = float(input('Digite a nota da terceira prova: '))
    media = (prova1 + prova2 + prova3) / 3
    if media >= 6 and faltas <= 15:
        print(f'Aprovado, a média foi de {media}.')
    if media >= 3 and media < 6:
        prova4 = float(input('Aluno em recuperação, insira a nota da quarta prova: '))
        media2 = (prova1 + prova2 + prova3 + prova4) / 4
        if media2 >= 5:
            print(f'Aprovado, a média foi de {media2}.')
        else:
            print(f'Aluno reprovado, a média foi de {media2}.')    
    elif media < 3 or faltas > 15:
        print(f'Reprovado, a média foi de {media}.')
    
aprovacao()