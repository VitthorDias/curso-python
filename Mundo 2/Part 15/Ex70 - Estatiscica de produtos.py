from termcolor import colored

print("-=" * 20)
print(colored(f"{'LOJA SE FUFU':^40}", 'blue'))
print("-=" * 20)

barato = caro = qtd = total = 0
nbarato = ' '
while True:
    produto = str(input("Nome do produto: ").strip().title())
    preco = float(input("Preco do produto: R$"))
    total += preco
    qtd += 1

    if preco > 1000:
        caro += 1
    if qtd == 1 or preco < barato:
        barato = preco
        nbarato = produto

    a = ' '
    while a not in "SN":
        a = str(input("Quer continuar[S/N]? ").upper().strip()[0])
    print(f'{"-§--§-":^40}')

    if a == "N":
        break

print("-" * 40)
print(f"Valor total da compra: R${total:.2f}.")
print(f"Quantidades de itens acima de R$1000,00: {caro}.")
print(f"Produto mais barato foi {nbarato} no valor de R${barato:.2f}.")
