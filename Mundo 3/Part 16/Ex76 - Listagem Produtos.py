itens = ("Lápis", 1.75, "Borracha", 2, "Caderno", 15.9, "Estojo", 25, "Transferidor", 4.2,
         "Compasso", 9.99, "mochila", 120.32, "Canetas", 22.3, "Livro", 34.9)

print("=" * 46)
print(f"{'LISTAGEM DE PRODUTOS':^46}")
print("=" * 46)

for i in range(0, len(itens), 2):
    print(f"{itens[i]:.<36} R${itens[i + 1]:>7.2f}")

print("=" * 46)