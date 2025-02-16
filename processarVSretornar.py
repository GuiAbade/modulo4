# Processar VS Retornar
# Função que apenas processa dados
print('Olá!')
# Funções que retornam dados
cidade = input('Qual é a sua cidade? ')
# Como escolher entre funções que processam VC retornam dados?
'''
Vou precisar usar essa informação na logica do programa ainda?
OU preciso processar esse dado, mas não irei utilizar mais ele depois?
'''


def exibir_cocacao_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)


exibir_cocacao_do_dia('usd')


def obter_cotacao_do_dia(moeda):
    if moeda == 'usd':
        return 5.57


cotacao = obter_cotacao_do_dia('usd')
if cotacao > 5:
    print('Investir em acoes americanas ')
else:
    print('Cotação não é favoravel!')
