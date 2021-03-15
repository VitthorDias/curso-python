prev = list()
dados = list()
ma = me = 0
while True:
    prev.append(str(input("Nome: ").strip().title()))
    prev.append(float(input("Peso: ").strip()))
    if len(dados) == 0:
        ma = me = prev[1]
    elif prev[1] > ma:
        ma = prev[1]
    elif prev[1] < me:
        me = prev[1]
    dados.append(prev.copy())
    prev.clear()

    opt = " "
    while opt not in 'SN':
        opt = str(input("Quer continuar? [S/N} ").upper().strip()[0])
    if opt == 'N':
        break

    print(f"{'--------':^25}")

print("=-=" * 25)
print(f"Foram adicionados {len(dados)} pessoas.")

print(f'O maior peso foi {ma}kg. Peso de ', end='')
for i in dados:
    if ma == i[1]:
        print(i[0], end='.. ')

print()
print(f'O menor peso foi {me}kg. Peso de ', end='')
for i in dados:
    if me == i[1]:
        print(i[0], end='.. ')
