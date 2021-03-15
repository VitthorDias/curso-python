from time import sleep

num1 = float(input("Primeiro número: "))
num2 = float(input("Segundo número: "))
option = 0
while option != 5:
    option = int(input("O que deseja fazer com eles?\n"
                       "        [1] SOMA.\n"
                       "        [2] MULTIPLICAÇÃO.\n"
                       "        [3] MAIOR.\n"
                       "        [4] NOVOS NÚMEROS.\n"
                       "        [5] SAIR.\n"
                       "---> "))

    if option == 1:
        print(f"{num1} + {num2} = {num1 + num2}\n")
    elif option == 2:
        print(f'{num1} X {num2} = {num1 * num2}\n')
    elif option == 3:
        if num1 > num2:
            print(f"Maior número: {num1:.0f}\n")
        elif num1 < num2:
            print(f"Maior número: {num2:.0f}\n")
        else:
            print("São iguais.\n")
    elif option == 4:
        num1 = float(input("Primeiro número: "))
        num2 = float(input("Segundo número: "))
    elif option == 5:
        print("\033[1:31mSAINDO...")
    else:
        print("\033[1:31mOpção invalida...")
    sleep(1)
