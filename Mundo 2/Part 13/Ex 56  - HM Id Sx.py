for i in range(1, 5):
    print(f"----{i}ª pessoa----")
    nome = str(input("Nome da pessoa: ").strip())
    idade = int(input("Idade da pessoa: "))
    sexo = str(input("Sexo M/F: ").lower().strip())
    print('\n')

    if i == 1:
        media = idade
        wmen = 0
        if sexo == 'm':
            velho = nome
            men = idade
        elif idade < 20:
            wmen = 1
    else:
        media += idade
        if sexo == 'm' and idade > men:
            velho = nome
        if sexo == 'f' and idade < 20:
            wmen += 1
print(f"Média de idade do grupo: {(media / 4):.1f}")
print(f"Homem mais velho: {velho.title()}")
print(f"Quantidade de mulheres abaixo de 20 anos: {wmen}")
