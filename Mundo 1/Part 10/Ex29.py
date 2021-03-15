km = int(input("Qual a velocidade do carro?"))

if km>80:
    print("=" * 100)
    print("Você foi multado por ultrapassar a velocidade de 80km/h.")
    print(f"Valor da multa R${((km - 80) * 7):.2f}.")
print("=" * 100)
