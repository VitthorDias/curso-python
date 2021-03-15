from time import sleep

a = float(input("Digite o primeiro lado do triângulo:"))
b = float(input("Digite o segundo lado do triângulo:"))
c = float(input("Digite o terceiro lado do triângulo:"))
print("\033[4;31mAnalisando...\n\033[m")
sleep(2)

cor = {'mg': '\033[1;35m', 'v': '\033[1;31m', 'clear': '\033[m'}
print("=" * 50)
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print(f"{cor['mg']}Forma um triângulo {cor['v']}EQUILÁTERO{cor['clear']}.")
    elif a == b or a == c or b == c:
        print(f"{cor['mg']}Forma um triângulo {cor['v']}ISÓSCELES{cor['clear']}.")
    else:
        print(f"{cor['mg']}Forma um triângulo {cor['v']}ESCALENO{cor['clear']}.")
else:
    print("Não forma um triângulo!")
print("=" * 50)
