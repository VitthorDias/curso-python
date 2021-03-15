def leiaInt(msg):
    from termcolor import colored

    val = False
    while not val:
        n = str(input(msg))
        if n.isnumeric():
            val = True
            n = int(n)
            return n
        else:
            print(colored('ERRO. Digite um número arquivo!!!', 'red'))


# Programa Principal
n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}.")
