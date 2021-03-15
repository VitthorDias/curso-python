matriz = [[], [], []]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Digite o valor para a posição [{i},{j}]: ").strip()))

print("===" * 30)

for i in range(0, 3):
    for j in range(0, 3):
        print(f"[{matriz[i][j]:^5}]", end=' ')
    print()
