from random import randint
from time import sleep

cont = 0
while True:
    num = int(input("Digite um número: "))
    pc = randint(0, 10)
    total = num + pc
    escolha = ' '

    while escolha not in "PI":
        escolha = str(input("Você quer par ou ímpar[P/I]? ").upper().strip()[0])

    print("-=-" * 20)
    print(f"Você jogou {num} e o computador {pc} e deu {num + pc}", end=' ')
    print("deu PAR." if total % 2 == 0 else "deu ÍMPAR.")
    print("-=-" * 20)

    if escolha == "P":
        if total % 2 == 0:
            print("\033[35mVocê Venceu!!")
            print("Vamos novamente.\033[m\n")
            sleep(1)
        else:
            print("\033[31mVocê PERDEU!!\033[m")
            sleep(2)
            break

    elif escolha == "I":
        if total % 3 == 0:
            print("\033[35mVocê Venceu!!")
            print("Vamos novamente.\033[m\n")
            sleep(1)
        else:
            print("\033[31mVocê PERDEU!!\033[m")
            sleep(2)
            break
    cont += 1

print("=" * 40)
print(f"Você venceu {cont} vezes.")
print("=" * 40)
