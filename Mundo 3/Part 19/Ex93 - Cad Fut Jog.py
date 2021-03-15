jogador = dict()
gol = list()
jogador['Nome'] = str(input("Nome: ").strip().title())
partidas = int(input("Quantas partidas? "))

for i in range(0, partidas):
    gol.append(int(input(f"  -Gols na {i + 1}º partida: ").strip()))

jogador['Gols'] = gol[:]
jogador['Total'] = sum(gol)
print("-=-" * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print("-=-" * 20)
print(f"O jogador {jogador['Nome']} jogou {len(jogador['Gols'])}")
for k, v in enumerate(jogador['Gols']):
    print(f'    =>Na partida {k + 1}, fez {v} goals.')
print(f"Fez um total de {jogador['Total']}")
