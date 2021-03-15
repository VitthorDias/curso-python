pessoas = {'nome': 'Vitthor', 'sexo': 'M', 'idade': 22}
print(pessoas)
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print()

del pessoas['sexo']
for k in pessoas.keys():
    print(k)

print()
for v in pessoas.values():
    print(v)

pessoas['idade'] = 20
pessoas['peso'] = 53
print()
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Goias', 'sigla': 'GO'}
estado2 = {'uf': 'Mato Grosso', 'sigla': 'MT'}
brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print(estado2)
print(brasil)
print(brasil[0]['uf'])
print(brasil[0]['sigla'])
