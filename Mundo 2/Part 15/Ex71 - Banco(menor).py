print("=" * 40)
print(f'\n{"BANCO FALENCIA" :^40}\n')
print("=" * 40)

saque = int(input("Deseja sacar qual valor? R$"))
cont = saque
ced = 50
tced = 0

print("\033[35m")
while True:
    if cont >= ced:
        cont -= ced
        tced += 1
    else:
        if tced > 0:
            print(f"Total de {tced} notas de R${ced}.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        tced = 0
        if cont == 0:
            break

print("\033[m", end='')
print("=" * 40)
print("Volte sempre ao BANCO FALENCIA.")
