#Solicitar o nome do produto, descrição, preço e validade. Apresentar na tela os dados recebidos.
import os

def funcproduto():
    nome_produto = input('Digite o nome do produto: ')
    descricao_produto = input('Digite a descrição do produto: ')
    preco_produto = float(input('Digite o valor do produto: R$ '))
    validade_produto = input('Digite a validade do produto: ')

    os.system('cls')
    print(f'Nome: {nome_produto}\nDescrição: {descricao_produto}\nvalor: R$ {preco_produto}\nValidade: {validade_produto}')

funcproduto()