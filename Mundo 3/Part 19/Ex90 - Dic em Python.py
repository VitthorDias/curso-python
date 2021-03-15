aluno = dict()
aluno['Nome'] = str(input("Nome: ").strip().title())
aluno['Media'] = float(input(f"Média de {aluno['Nome']}: ").strip())
if aluno['Media'] >= 6:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = "Reprovado"

print("-=-" * 30)
for k, v in aluno.items():
    print(f"{k} é igual a {v}")
