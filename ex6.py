#Calcular a soma dos 100 primeiros números (0 a 100).

def funcloop():

    soma = 0
    for i in range(101):
        soma += i
        print(soma)
    
funcloop()