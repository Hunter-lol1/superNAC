#Que gere o preço de um carro ao consumidor e os valores pagos pelo imposto e pelo lucro do distribuidor, sabendo o custo de fábrica do carro e que são pagos: a) de imposto: 45% sobre o custo do carro; b) de lucro do distribuidor: 12% sobre o custo do carro.

def análcarro():

    valor_carro = float(input('Digite o valor do carro que deseja comprar: '))

    imposto = valor_carro * 0.45
    lucro = valor_carro * 0.12

    print(f'De acordo com o valor de R$ {valor_carro} você pagaria R$ {imposto} de imposto e a empresa teria R$ {lucro} de lucro')

análcarro()