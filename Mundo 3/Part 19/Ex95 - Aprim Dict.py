jogador = dict()
time = list()
gol = list()
while True:
    jogador.clear()
    gol.clear()
    jogador['Nome'] = str(input("Nome: ").strip().title())
    partidas = int(input("Quantas partidas? "))
    for i in range(0, partidas):
        gol.append(int(input(f"  -Gols de {jogador['Nome']} na {i + 1}º partida: ").strip()))
    jogador['Gols'] = gol[:]
    jogador['Total'] = sum(gol)
    time.append(jogador.copy())

    while True:
        opt = str(input("Deseja continuar [S/N]? ").upper().strip()[0])
        if opt in 'SN':
            break
    if opt == 'N':
        break
    print("---" * 20)

print("-=-" * 20)
print('Cod', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print("===" * 20)
for k, v in enumerate(time):
    print(f"{k:>4}", end=' ')
    for a in v.values():
        print(f'{str(a):<15}', end='')
    print()

print("-=-" * 20)
while True:
    busca = int(input("Mostrar os dados de qual jogador (999 para sair)? ").strip())
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print("Jogador inválido..")
    else:
        print(f'Levantamento do jogador {time[busca]["Nome"]}')
        for pos, dad in enumerate(time[busca]['Gols']):
            print(f'    =>Na partida {pos + 1}, fez {dad} gols. ')
        print("--" * 20)
