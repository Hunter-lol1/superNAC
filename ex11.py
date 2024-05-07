#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

def comissao():
    vendas = []
    for total_vendas in range(5):
        venda = float(input('Digite o valor da venda deste vendedor: '))
        vendas.append(venda)
    total_vendas = sum(vendas)
    if total_vendas <= 1500.00:
        salario = total_vendas + (total_vendas * 0.03)
        print(f'O salário do funcionário é: {salario}')
    elif total_vendas > 1500.0:
        salario = total_vendas + (total_vendas * 0.05)
        print(f'O salário do funcionário é: {salario}')

comissao()