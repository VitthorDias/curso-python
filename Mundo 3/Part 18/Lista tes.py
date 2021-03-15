pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0][0])  # Pedro
print(pessoas[1][1])  # 19
print(pessoas[2][0])  # João
print(pessoas[1])  # ['Maria', 19]

print("=-=" * 30)

teste = list()
teste.append("Gustavo")
teste.append(40)
galera = list()
galera.append(teste.copy())
teste[0] = "Maria"
teste[1] = 22
galera.append(teste.copy())
print(galera)
