# Objetivo desta aula é refazer a aula sobre turtle otimizando com funções.
from turtle import Turtle

t = Turtle()
t.speed(1)


def se_virar_esquerda(t):
    valor_qtts_graus_rotacionar = int(
        input('Quanto graus(º) desea rotacionar para esquerda? :'))
    t.left(valor_qtts_graus_rotacionar)


def virar_direita(t):
    valor_qtts_graus_rotacionar = int(
        input('Quanto graus(º) desea rotacionar para esquerda? :'))
    t.right(valor_qtts_graus_rotacionar)


def deslocando_frente(t):
    qtt_px_deslocar = int(
        input('Informe quantos pixel deseja deslocar para frente:  '))
    t.forward(qtt_px_deslocar)


def deslocando_tras(t):
    qtt_px_deslocar = int(
        input('Informe quantos pixel deseja deslocar para tras:  '))
    t.backward(qtt_px_deslocar)


# verificando se o usuário deseja rotacionar antes de deslocar
while True:
    valor_deseja_rotacionar = input('Você deseja rotacionar? [s/n]: ')
    # caso sim, iremos verificar para qual direção rotacionar...
    if valor_deseja_rotacionar == 's':
        while True:
            valor_direcao_da_rotação = input(
                'Para qual lado deseja rotacionar? [e/d]: ')

            if valor_direcao_da_rotação == 'e':
                se_virar_esquerda(t)
                break
            elif valor_direcao_da_rotação == 'd':
                virar_direita(t)
                break
            else:
                print('Corrija o comando!')
    elif valor_deseja_rotacionar == 'n':
        pass

    # verificando se o usuário deseja se deslocar...
    valor_se_deseja_deslocar = input('Deseja deslocar? [s/n]: ')

    if valor_se_deseja_deslocar == 's':
        while True:
            valor_frente_ou_tras = input(
                'Deseje descolar para FRENTE(f) ou para TRAS(t)? [f/t]: ')

            if valor_frente_ou_tras == 'f':
                deslocando_frente(t)
                break
            elif valor_frente_ou_tras == 't':
                deslocando_tras(t)
                break
            else:
                print('Corrija o comando!')
    elif valor_se_deseja_deslocar == 'n':
        break
    deseja_continuar = input('Deseja continuar?: [s/n]: ')
    if deseja_continuar == 's':
        continue
    else:
        print('Até a próxima...!')
        break
