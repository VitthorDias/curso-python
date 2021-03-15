num = [[], []]
for i in range(1, 8):
    n = int(input(f"Digite o {i}º valor: ").strip())
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)

print("=-=" * 30)
print(f"Os valores pares digitados foram: {sorted(num[0])}")  # Ou uso o num[0].sort() e nesse print só num[0]
print(f"Os valores impares digitados foram: {sorted(num[1])}")  # Ou uso o num[1].sort() e nesse print só num[1]
