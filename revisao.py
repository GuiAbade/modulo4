def somar(*valores, b):
    print(valores)
    for valor in valores:
        b += valor
    print(b)


# Os valores que estão sem parâmetros
# Aparentes são passados em formato de túpla(um tipo de lista)
somar(5, 10, 20, b=5)
# *args
# Inicia um parametro com um * definindo 
# Assim podemos receber uma quantidade variável de argumentos para o mesmo parâmetro