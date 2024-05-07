#Calcular a quantidade de dinheiro gasto por um fumante. Dados: o número de anos que ele fuma, o nº de cigarros fumados por dia e o preço de uma carteira com 20 cigarros.

def calcfumante():

    anos = int(input('Digite há quantos anos você fuma: '))
    qtd_cigarros_dia = int(input('Digite quantos cigarros você fuma por dia: '))
    valor_maco = float(input('Digite o valor do maço com 20 cigarros: '))

    total_cigarros = anos * 365 * qtd_cigarros_dia
    macos_comprados = total_cigarros / 20
    total_gasto = macos_comprados * valor_maco

    print(f'O valor gasto em {anos} anos foi de R$ {total_gasto}')

calcfumante()