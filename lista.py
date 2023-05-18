# Criando uma lista de compras vazia
lista_de_compras = []

# Loop para adicionar itens à lista de compras
while True:
    # Pedindo ao usuário para digitar um item ou "fim" para encerrar
    item = input("Digite um item para adicionar à lista de compras (ou 'fim' para encerrar): ")
    
    # Verificando se o usuário digitou "fim"
    if item.lower() == 'fim':
        break
    
    # Adicionando o item à lista de compras
    lista_de_compras.append(item)

# Imprimindo a lista de compras
print('Lista de compras:')
for item in lista_de_compras:
    print('-', item)