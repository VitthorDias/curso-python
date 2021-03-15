alunos = list()
nome = list()
nota = list()

while True:
    nome = (str(input("Nome: ").strip().title()))
    nota1 = (float(input("Nota 1: ").strip()))
    nota2 = (float(input("Nota 2: ").strip()))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])

    opt = ' '
    while opt not in 'SN':
        opt = str(input("Você deseja continuar? [S/N] ").upper().strip()[0])
    if opt == "N":
        break


print("=" * 50)
print(f"{'Nº':<4} {'NOME':<10} {'MEDIA':>8}")
for p, i in enumerate(alunos):
    print(f'{p:<4} {i[0]:<10} {i[2]:>8.1f}')

print("=" * 50)
num = 0
while True:
    num = int(input("Quer ver a nota de qual aluno? 999 para para: ").strip())
    if num == 999:
        break
    if num <= len(alunos) - 1:
        print(f"As notas de {alunos[num][0]} foram {alunos[num][1]}.")
        print()

print("-" * 50)
print("\n\033[1;31mFINALIZANDO...")
