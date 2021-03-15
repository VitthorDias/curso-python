palavras = ('abacate', 'avestruz', 'computador', 'vitthor', 'mercado', 'python', 'estudanto')

for i in palavras:
    print(f"\nA palavra {i.upper()} tem as vogais ", end='')
    for vogal in i:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
