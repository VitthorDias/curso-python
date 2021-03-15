num = list()
print("==" * 20)
for i in range(0, 5):
    num.append(int(input(f"Digite um número para a posição {i}: ")))

print("==" * 20)
print(f"Maior: {max(num)} nas posições", end=' ')
for p, i in enumerate(num):
    if i == max(num):
        print(f'{p}..', end=' ')

print(f"\nMenor: {min(num)} nas posições", end=' ')
for p, i in enumerate(num):
    if i == min(num):
        print(f'{p}..', end=' ')

print()
print("==" * 20)
