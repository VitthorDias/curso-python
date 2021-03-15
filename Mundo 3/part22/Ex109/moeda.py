def aumentar(valor=0, porc=1, form=False):
    res = valor * ((porc / 100) + 1)
    return res if not form else moeda(res)


def dobro(valor=0, form=False):
    res = valor * 2
    return res if not form else moeda(res)


def diminuir(valor=0, porc=1, form=False):
    res = valor * (1 - (porc / 100))
    return res if not form else moeda(res)


def metade(valor=0, form=False):
    res = valor / 2
    return res if not form else moeda(res)


def moeda(valor=0):
    return f'R${valor:.2f}'.replace('.', ',')
