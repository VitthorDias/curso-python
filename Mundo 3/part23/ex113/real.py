def leiaReal(msg):
    from termcolor import cprint

    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            cprint("ERRO: Por favor, digite um número arquivo válido.", 'red')
            continue
        except KeyboardInterrupt:
            cprint("Entrada de dados interrompida pelo usuário.", 'red')
            return 0
        else:
            return num
