# Desafio 1
# Desafio 🥇
'''
Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:
1 - O primeiro argumento deve ser posicional
2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
'''


def gerar_objeto(cor, *, altura, formato):
    print(
        f'A cod do seu objeto é {cor}, a altura é {altura} e o formato é {formato}')


gerar_objeto('amarelo', altura=1.80, formato='quadrado')
