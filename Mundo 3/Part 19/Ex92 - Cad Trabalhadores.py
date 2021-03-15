from datetime import datetime

cad = dict()
cad['Nome'] = str(input("Nome: ").strip().title())
ano = int(input("Ano de nascimento: ").strip())
cad['Idade'] = datetime.now().year - ano
cad['Ctps'] = int(input("Carteira de trabalho (0 não tem): ").strip())

if cad['Ctps'] != 0:
    cad['Contratação'] = int(input("Ano de contratação: ").strip())
    cad['Salário'] = float(input("Salário: R$").strip())
    cad['Aposentadoria'] = (cad['Contratação'] + 35) - ano

print("==¨==" * 10)
for k, v in cad.items():
    print(" " * 5, end='')
    if k.lower() == 'salário':
        print(f"--{k} tem o valor R${v}.")
    else:
        print(f"--{k} tem o valor {v}.")
