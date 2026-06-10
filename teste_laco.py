encomendas = input("Digite os números das encomendas separados por vírgula: ").split(',')
try:
    for encomenda in encomendas:
        print(int(encomenda.strip()))
except ValueError:
    print("Uma das entradas não é um número válido.")