from time import sleep

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
print("\n\033[4;34mCalculando a média...\033[m\n")
sleep(2)

media = (n1 + n2 + n3) / 3
print(f"A média do aluno é {media:.1f}")
if media < 5:
    print("\033[1;31mREPROVADO!!!")
elif 5 <= media <= 6.9:
    print("\033[1;33mRECUPERAÇÃO!!!")
else:
    print("\033[1;36mAPROVADO!!!")
