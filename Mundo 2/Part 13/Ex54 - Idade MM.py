from datetime import date

maior, menor = 0, 0
for i in range(1, 8):
    ano = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    idade = date.today().year - ano
    if idade > 20:
        maior += 1
    else:
        menor += 1

print(f"Maiores de idade: {maior}")
print(f'Menores de idade: {menor}')
