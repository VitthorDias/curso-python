pessoa = dict()
cadastro = list()
som = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome: ").strip().title())

    while True:
        pessoa['Sexo'] = str(input("Sexo [F/M]: ").strip().upper()[0])
        if pessoa['Sexo'] in "FM":
            break
        print("Sexo invalido...")

    pessoa['Idade'] = int(input("Idade: ").strip())
    som += pessoa['Idade']
    cadastro.append(pessoa.copy())

    while True:
        opt = str(input("Deseja continuar [S/N]? ").strip().upper()[0])
        if opt in 'SN':
            break
        print("Opção inválida..")
    if opt == 'N':
        break
    print("--" * 20)

print("==" * 20)
media = som / len(cadastro)
print(f"Foram cadastradas {len(cadastro)} pessoas.")
print(f'A média das idade é {media:.2f}.')
print(f"Mulheres cadastradas: ", end='')
for v in cadastro:
    if v['Sexo'] == 'F':
        print(f'[{v["Nome"]}]', end=' ')
print()

print("Pessoas acimas da média: ")
for c in cadastro:
    if c['Idade'] >= media:
        print('    ', end='')
        for k, v in c.items():
            print(f'{k} = {v}', end=', ')
        print()

print("-=-=-=-= FINALIZADO =-=-=-=-")
