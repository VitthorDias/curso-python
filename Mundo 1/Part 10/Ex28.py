from random import randint
from time import sleep

pc = randint(0, 5)
player = int(input("Qual número eu pensei entre 0 e 5? "))
print("Processando...")
sleep(2)
if player == pc:
    print("Parabéns. Você acertou \U0001F60A.")
else:
    print(f"Você errou \U0001F60C. Pensei no {pc}")
