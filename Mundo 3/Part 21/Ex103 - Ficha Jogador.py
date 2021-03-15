def ficha(nome='<desconhecido>', gols=0):
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


nam = str(input("Nome do Jogador: ").title().strip())
gol = str(input("Número de Gols: "))
if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
if nam == '':
    print(ficha(gols=gol))
else:
    print(ficha(nam, gol))
