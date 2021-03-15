num = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
c = 1
pa = num
while c <= 10:
    print(f"Termo {c}: {pa}")
    pa += razao
    c += 1
