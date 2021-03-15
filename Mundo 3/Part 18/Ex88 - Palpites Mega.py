from random import randint
from time import sleep

print("=" * 40)
qtd = int(input("Quantos jogas deseja sortear? "))
print(f"\n{'-=-=-=-=- SORTEANDO -=-=-=-=-':^40}\n")

games = []
num = []
for i in range(0, qtd):
    st = 0
    while st < 6:
        n = randint(1, 60)
        if n not in num:
            num.append(n)
            st += 1

    num.sort()
    games.append(num.copy())
    num.clear()
    print(f"Jogo {i + 1}: {games[i]}")
    sleep(1)

print("=" * 40)
print(f"{'BOA SORTE':^40}")
print("=" * 40)
