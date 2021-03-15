a = float(input("Digite o primeiro lado do triângulo:"))
b = float(input("Digite o segundo lado do triângulo:"))
c = float(input("Digite o terceiro lado do triângulo:"))

print("=" * 50)
if a + b > c and b + c > a and a + c > b:
    print("Forma um triângulo!")
else:
    print("Não forma um triângulo!")
print("=" * 50)
