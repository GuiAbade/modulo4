# Decorators
def meu_decorator(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper


@meu_decorator
def parabeinzar():
    print('Parabéns!!!')


# Equivale ao @meu_decorator
""" resultado = meu_decorator(parabeinzar)
resultado() """
