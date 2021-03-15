num = list()
for i in range(0, 5):
    prev = int(input("Digite um número: "))

    if i == 0 or prev > num[-1]:
        num.append(prev)
        print("Adicionado no final da lista..")
        print(f'{"---":^30}')
    if num.count(prev) == 0:
        if prev < num[0]:
            num.insert(0, prev)
            print(f'Adicionado na posição 0.. ')
            print(f'{"---":^30}')
        else:
            temp = 0
            for a in range(0, len(num)):
                if prev > num[a]:
                    temp = a + 1

            num.insert(temp, prev)
            print(f'Adicionado na posição {temp}.. ')
            print(f'{"---":^30}')

print("-=" * 30)
print(f'Os valores digitados foram {num}.')