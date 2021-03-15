from random import randint
from time import sleep
from operator import itemgetter

ranking = list()
players = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}

for k, v in players.items():
    print(f"O {k} tirou {v}")
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print("==" * 20)
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]}.")
    sleep(1)
