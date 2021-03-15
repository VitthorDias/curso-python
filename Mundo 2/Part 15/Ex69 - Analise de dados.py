cont = men = wo = 0
while True:
    print("=" * 40)
    print(f'{"CADASTRAR UMA PESSOA":^40}')
    print("=" * 40)
    idade = int(input("Quantos anos tem? "))

    while True:
        sexo = str(input("Sexo da pessoa [M/F]: ").upper()[0])
        if sexo in 'MF':
            break

    if idade > 18:
        cont += 1
    if sexo in 'M':
        men += 1
    elif idade < 20:
        wo += 1

    while True:
        option = str(input("Deseja cadastras mais [S/N]?").upper()[0])
        if option in 'SN':
            break

    if option in 'N':
        break

print("=" * 40)
print(f"Maiores de 18 anos: {cont}")
print(f"Homens cadastrados: {men}")
print(f"Mulheres abaixo de 20 anos: {wo}")
print("=" * 40)
