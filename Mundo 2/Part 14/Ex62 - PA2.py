num = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
pa = num
mais = 10
total = 0
cont = 1
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{pa} ", end=' ')
        pa += razao
        cont += 1
    print("PAUSA.")
    mais = int(input("\nQuer ler mais quantos termos? "))
print("\nFinalizado")
