t1 = int(input("Digite um termo: "))
raz = int(input("Digite a razão: "))

s = t1
for i in range(1, 11):
    if i == 1:
        print(f"Termo {i}: {s}")
    else:
        s += + raz
        print(f'Termo {i}: {s}')
