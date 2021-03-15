casa = float(input("Valor da casa R$"))
salario = float(input("Salário do comprador: R$"))
anos = int(input("Quantos anos de financiamento? "))

parc = (casa / (anos * 12))
print("=" * 100)
if parc > (0.3 * salario):
    print(f"O valor da parcela mensal ficou R${parc:.2f} e excete 30% do seu salário(R${(salario * 0.3):.2f}).")
    print("\033[1;31mEMPRÉSTIMO NEGADO!!!\033[m")
else:
    print(f"Valor da parcela mensal ficou em R${parc:.2f}.")
    print(("\033[1;32mEMPRÉSTIMO ACEITO!!!\033[m"))
print("=" * 100)
