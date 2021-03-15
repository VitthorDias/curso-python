valor = (int(input("Digite um valor: ")),
         int(input("Digite outro valor: ")),
         int(input("Digite mais um valor: ")),
         int(input("Digite o ultimo valor: ")))
print("-=" * 30)
print(f"Você digitou os números {valor}.")
print("-=" * 30)
print(f'Apareceu o 9: {valor.count(9)} vezes.')
if valor.count(3) > 0:
    print(f"O primeiro 3 está na {valor.index(3) + 1 }ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print("Números pares: ", end='')
for i in valor:
    if i % 2 == 0:
        print(i, end=" ")
