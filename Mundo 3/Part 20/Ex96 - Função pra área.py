def area(l, c):
    print(f'A área do terreno {l}x{c} é de {l * c} m².')


print(f"{'CONTROLE DE ÁREA':^40}")
print("-" * 40)
larg = float(input("Largura (m): ").strip())
comp = float(input("Comprimento (m): ").strip())

area(larg, comp)
