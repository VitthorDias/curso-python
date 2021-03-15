num = list()
while True:
    num.append(int(input("Digite um valor: ")))

    opt = " "
    while opt not in "SN":
        opt = str(input("Você quer continuar[S/N]? ").upper().strip()[0])

    if opt == "N":
        break

num.sort(reverse=True)
print("-=" * 30)
print(f"Foram digitados {len(num)}.")
print(f"Números em ordem decrescente: {num}")
if 5 in num:
    print("O valor 5 faz parte da lista")
else:
    print("O valor 5 não faz parte da lista")
