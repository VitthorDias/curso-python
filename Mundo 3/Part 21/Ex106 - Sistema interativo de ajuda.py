from termcolor import cprint


def ajuda(com):
    from time import sleep
    titulo(f'Analisando o manual do comando {com}...', 5, 6)
    sleep(2)
    print('\033[7;30m')
    help(com)
    print('\033[m')
    sleep(4)


def titulo(t, c1, c2):
    cor = ['white', 'on_red', 'blue', 'on_grey', 'on_blue', 'yellow', 'on_cyan']
    tm = len(t) + 5

    cprint("\033[1m=" * tm, cor[c1], cor[c2])
    cprint(f'\033[1m{t.center(tm)}', cor[c1], cor[c2])
    cprint("\033[1m=" * tm, cor[c1], cor[c2])


# Principal
comando = ''
while True:
    titulo("Sistema interativo PyHelp.", 2, 3)
    comando = str(input("\033[1;31mFunção ou biblioteca >>\033[m "))
    if comando.upper() == "FIM":
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 0, 1)
