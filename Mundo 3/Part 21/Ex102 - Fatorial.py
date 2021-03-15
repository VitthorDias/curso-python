def fatorial(num, show=False):
    """
    => Calcular o fatorial de um número.
    :param num: Valor a ser fatorado.
    :param show: (opcional) Mostrar ou não a calculo. False por padrão.
    :return: Retorna o resultado da conta.
    """
    f = 1
    for i in range(num, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f


print(fatorial(5, show=True))
help(fatorial)
