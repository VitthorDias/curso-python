def aumentar(valor=0, porc=1):
    res = valor * ((porc / 100) + 1)
    return res


def dobro(valor=0):
    res = valor * 2
    return res


def diminuir(valor=0, porc=1):
    res = valor * (1 - (porc / 100))
    return res


def metade(valor=0):
    res = valor / 2
    return res


def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')
