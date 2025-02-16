# O asteristico obriga que use a palavra chave mandatória ao usar a função
def exibir_preco(nome_produto, *, preco):
    print(f'{nome_produto} está no valor de {preco}')


exibir_preco(nome_produto='abacate', preco=5.80)
# OU
# Argumentos nomeados:
exibir_preco(nome_produto='abacate', preco=5.80)
