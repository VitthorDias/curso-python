s = 0
for i in range(1, 7):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        s += num
print(f"\nA soma dos números pares é {s}.")
