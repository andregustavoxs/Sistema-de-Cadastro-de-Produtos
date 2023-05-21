# Criando um dicionário de compras vazio
# Os nomes dos produtos serão as chaves, enquanto suas quantidades serão os valores dessas chaves
lista_de_compras = {}

# Loop para adicionar itens à lista de compras
while True:
    # Pedindo ao usuário para digitar um item ou "fim" para encerrar
    item = input("Digite um item para adicionar à lista de compras (ou 'fim' para encerrar): ").capitalize()
    
    # Verificando se o usuário digitou "fim"
    if item.lower() == 'fim':
        break

    # Pedindo ao usuário para digitar a quantidade do item
    quantidade = input(f"Digite a quantidade de {item} que deseja à lista de compras: ")

    # Verifica se a quantidade não é um número ou se a quantidade é 0 ou negativa
    # Se sim, pede novamente para digitar as informações
    if not quantidade.isnumeric() or int(quantidade) <= 0:
        print("O valor digitado é inválido! Por favor, digite uma quantidade válida: ")
        continue
    
    # Adicionando o item à lista de compras, com sua respectiva quantidade
    lista_de_compras[item] = quantidade

# Imprimindo a lista de compras
print('Lista de compras:')
for item in lista_de_compras.keys():
    print(f'- {item} (x{lista_de_compras[item]})')

# Salvando a lista de compras em um arquivo de texto
nome_arquivo = 'lista_compras.txt'
with open(nome_arquivo, 'w', encoding="utf-8") as arquivo:
    for item in lista_de_compras.keys():
        arquivo.write(item + '(' + lista_de_compras[item] + ')' + '\n')
