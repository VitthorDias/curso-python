matriz = [[], [], []]

sp = st = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f'Digite o valor para a posição [{i}, {j}]: ')))
        if matriz[i][j] % 2 == 0:
            sp += matriz[i][j]

print("=-=" * 15)
for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^7}]", end=' ')
    print()
    st += matriz[i][2]

print("=-=" * 15)
print(f"A soma dos valores pares é {sp}.")
print(f'A soma dos valores da terceira coluna é {st}.')
print(f"O maior valor da segunda linha é {max(matriz[1])}")
