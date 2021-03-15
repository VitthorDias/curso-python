print("=" * 40)
print(f'\n{"BANCO FALENCIA" :^40}\n')
print("=" * 40)

saque = int(input("Deseja sacar qual valor? R$"))
cont = saque
test = 0

print("\033[35m")
while True:
    if test == 0:
        cinq = saque // 50
        cont -= cinq * 50
        if cinq > 0:
            print(f"Total de {cinq} notas de R$50.00.")
    elif test == 1:
        vint = cont // 20
        cont -= vint * 20
        if vint > 0:
            print(f"Total de {vint} notas de R$20.00.")
    elif test == 2:
        dez = cont // 10
        cont -= dez * 10
        if dez > 0:
            print(f"Total de {dez} notas de R$10.00.")
    elif test == 3:
        um = cont // 1
        cont -= um * 1
        if um > 0:
            print(f"Total de {um} notas de R$1.00.")
    else:
        print("\033[m", end='')
        print("=" * 40)
        print("Volte sempre ao BANCO FALENCIA.")
        break
    test += 1
