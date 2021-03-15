from time import sleep

def contador(i, f, p):
    print("=" * 50)
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print(f'Contando de {i} para {f} de {p} em {p}')
    if i < f:
        for num in range(i, f + 1, p):
            print(num, end=' ')
            sleep(0.5)
    elif i > f:
        for num in range(i, f - 1, -p):
            print(num, end=' ')
            sleep(0.5)
    print()


# Função Principal
contador(1, 10, 1)
contador(10, 0, 2)
a = int(input("Inicio: ").strip())
b = int(input("Fim: ").strip())
c = int(input("Passo: ").strip())
contador(a, b, c)
print("=" * 50)
