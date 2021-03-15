def leia_dinheiro(msg):
    from termcolor import cprint

    val = False
    while not val:
        num = str(input(msg)).replace(',', '.').strip()
        if num.isalpha() or num == '':
            cprint(f"ERRO! '{num}' é um preço inválido.", 'red')
        else:
            val = True
            return float(num)
