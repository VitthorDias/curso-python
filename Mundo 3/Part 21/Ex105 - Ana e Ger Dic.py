def notas(*n, sit=False):
    """
    =>Função para analisar as notas de um aluno.
    :param n: Notas a serem analisadas (Pode ser usada várias notas).
    :param sit: É opcional para mostrar a situação das notas.
    :return: Retorna um dicionário com as informações do aluno.
    """
    aluno = dict()
    aluno['Total'] = len(n)
    aluno['Maior'] = max(n)
    aluno['Menor'] = min(n)
    aluno['Media'] = sum(n) / len(n)
    if sit:
        if aluno['Media'] >= 7:
            aluno['Situação'] = 'BOM'
        elif 6 <= aluno['Media'] < 7:
            aluno['Situação'] = 'RAZOÁVEL'
        else:
            aluno['Situação'] = 'RUIM'
    return aluno


# Principal
al = notas(9, 5, 4, 10, sit=True)
print(al)
help(notas)
