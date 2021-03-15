num = list()
impar = list()
par = list()
while True:
    num.append(int(input("Digite um número: ")))

    opt = " "
    while opt not in "NS":
        opt = str(input("Deseja continuar [S/N]? ").upper().strip()[0])

    if opt == "N":
        break

for i in num:
    if i % 2 == 0:
        par.append(i)
    else:
        impar.append(i)

print("-=" * 30)
print(f"Os valor digitados foram: {num}")
print(f"Os valores pares foram: {par}")
print(f"Os valores impares foram: {impar}")
