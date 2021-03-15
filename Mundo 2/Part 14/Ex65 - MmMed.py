maior = menor = s = c = 0
i = ''
while i != 'N':
    n = int(input("Digite um número arquivo: "))
    i = str(input("Quer continuar N/S? ").upper())
    if c == 0:
        maior = menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c += 1
    s += n
print(f"\nVocê digitou {c} números.")
print(f"Maior: {maior}")
print(f"Menor: {menor}")
print(f"Soma: {s}")
print(f"Média: {(s / c):.3f}")
