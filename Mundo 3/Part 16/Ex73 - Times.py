times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza',
         'Goías', 'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense',
         'Botafogo', 'Ceará', 'Cruzeiro', 'CSA', 'Chapecoense', 'Avai')
print("-=-" * 20)
print(f"Coloção: {times}")
print("-=-" * 20)
print(f"Cinco primeiros colocados: {times[:5]}")
print("-=-" * 20)
print(f"Quatro ultimos colocados: {times[-4:]}")
print("-=-" * 20)
print(f'Times em ordem alfabetica: {sorted(times)}')
print("-=-" * 20)
print(f"A Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")
print("-=-" * 20)
