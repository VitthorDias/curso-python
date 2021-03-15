num = list()
while True:
    prev = int(input("Digite um número: "))
    if prev not in num:
        num.append(prev)
        print("Valor adicionado com sucesso...")
    else:
        print("Valor duplicado!! Não pode ser adicionado..")

    opt = ' '
    while opt not in 'SN':
        opt = str(input("Quer continuar[S/N]? ").upper().strip()[0])

    if opt == 'N':
        break

print('==' * 20)
print(f"Valores digitados: {sorted(num)}")
print('==' * 20)
