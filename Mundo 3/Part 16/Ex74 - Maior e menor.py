from random import randint

num = (randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10), randint(0, 10))
print("Números sorteados:", end=' ')
for n in range(0, 5):
    print(num[n], end=" ")

print(f"\nMaior: {max(num)}.")
print(f"Menor: {min(num)}.")
print(f'Ordenado: {sorted(num)}.')
