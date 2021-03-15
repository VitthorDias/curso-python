from termcolor import colored, cprint

from lib import arquivo


def leia_int(msg='', qtd=0, ver=False):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            cprint("ERRO! Digite um número inteiro válido.", 'red')
            continue
        else:
            if ver:
                if n not in range(1, qtd):
                    cprint("Opção inválida.", 'red')
                else:
                    print("-" * 50)
                    return n
            else:
                return n


def cabecalho(msg):
    tm = 50
    print("-" * tm)
    print(f"{msg.center(tm)}")
    print('-' * tm)


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    c = 1
    msg = colored("Sua opção: ", "green")
    for valor in lista:
        print(colored(c, 'yellow'), '-', colored(valor, 'blue'))
        c += 1
    print("-" * 50)
    return leia_int(msg, c, True)


def dados():
    nome = str(input("Nome: ")).title().strip()
    idade = leia_int("Idade: ", False)
    arquivo.escrever_arq('cursopython', nome, idade)


if __name__ == '__main__':
    pass
