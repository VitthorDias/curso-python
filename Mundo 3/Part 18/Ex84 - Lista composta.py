prev = list()
dados = list()
ma = me  = 0
while True:
    prev.append(str(input("Nome: ").strip().title()))
    prev.append(float(input("Peso: ").strip()))
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

for i in range(0, len(dados)):
    if i == 0:
        ma = dados[i][1]
        me = dados[i][1]
    elif dados[i][1] > ma:
        ma = dados[i][1]
    elif dados[i][1] < me:
        me = dados[i][1]

print(f'O maior peso foi {ma}kg. Peso de ', end='')
for p, i in enumerate(dados):
    if ma == dados[p][1]:
        print(dados[p][0], end='.. ')

print()
print(f'O menor peso foi {me}kg. Peso de ', end='')
for p, i in enumerate(dados):
    if me == dados[p][1]:
        print(dados[p][0], end='.. ')
