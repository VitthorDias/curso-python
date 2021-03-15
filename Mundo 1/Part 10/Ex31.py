km = float(input("Quantos KM de viagem? "))

print('=' * 100)
if km <= 200:
    print(f'Preço da passagem é de R${(km * 0.5):.2f}.')
else:
    print(f'Preço da passagem é de R${(km * 0.45):.2f}')
print('=' * 100)
