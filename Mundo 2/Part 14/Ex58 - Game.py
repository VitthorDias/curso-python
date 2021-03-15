from random import randint
from termcolor import colored

pc = randint(0, 10)
player = False
c = 0
print(colored("Pensei em um número entre 0 e 10. Tente adivinhar até acerta ai!! \n", 'magenta'))

while not player:
    num = int(input(colored("Qual número eu pensei? ", 'magenta')))
    c += 1
    if num == pc:
        player = True
    else:
        if pc > num:
            print("Mais... Tente novamente!!!")
        else:
            print("Menos... Tente novamente!!!")

print(colored(f"\nVocê acertou. Eu pensei no \033[31m{pc}\033[m.", 'magenta'))
print(colored(f"Porém foram necessárias {colored(c, 'red')} \033[35mtentativas.", 'magenta'))
