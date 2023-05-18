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

# Salvando a lista de compras em um arquivo de texto
nome_arquivo = 'lista_compras.txt'
with open(nome_arquivo, 'w') as arquivo:
    for item in lista_de_compras:
        arquivo.write(item + '\n')
