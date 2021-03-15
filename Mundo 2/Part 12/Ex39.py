from datetime import date
nasc = int(input("Em que ano você nasceu? "))

atual = date.today().year
anos = atual - nasc
cr = {"v": "\033[31m", "a": "\033[35m", "clear": "\033[m"}
print("\n")
if anos < 18:
    ano = 18 - anos
    print(f'{cr["a"]}Ainda faltam {ano} anos.')
    print(f'Seu alistamento será em {atual + ano}.{cr["clear"]}')
elif anos == 18:
    print(f'{cr["a"]}Você já tem 18 anos, está na hora de você se alistar.{cr["clear"]}')
else:
    ano = anos - 18
    print(f'{cr["a"]}Você deveria ter se alistado há {ano} anos. {cr["v"]}VÁ IMEDIATAMENTE SE ALISTAR.{cr["clear"]}')
