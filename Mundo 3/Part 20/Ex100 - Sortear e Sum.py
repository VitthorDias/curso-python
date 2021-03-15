from time import sleep
from random import randint


def sorteia():
    print("Sorteando 5 valores da lista: ", end='')
    n = 0
    while n != 5:
        st = randint(0, 10)
        num.append(st)
        print(st, end=' ')
        sleep(1)
        n += 1
    print()


def somaPar(num):
    soma = 0
    for v in num:
        if v % 2 == 0:
            soma += v
    print(f"Somando os valores pares de {num}, temos {soma}")


# Função Principal
num = list()
sorteia()
print("---" * 20)
somaPar(num)
