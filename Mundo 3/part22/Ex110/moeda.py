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


def resumo(valor, aum, dim):
    titulo()
    print(f"Preço analisado: \t\t\tR${valor}")
    print(f"Dobro do preço:  \t\t\t{dobro(valor, True)}")
    print(f"Metade do preço: \t\t\t{metade(valor, True)}")
    print(f"{aum}% de aumento: \t\t\t{aumentar(valor, aum, True)}")
    print(f"{dim}% de redução: \t\t\t{diminuir(valor, dim, True)}")
    print("=" * 40)


def titulo():
    print('=' * 40)
    print(f'{"RESUMO DO VALOR".center(40)}')
    print("=" * 40)
