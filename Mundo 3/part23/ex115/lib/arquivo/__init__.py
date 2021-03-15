from lib import sistema
from termcolor import cprint


def ver_arq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        exit()
    else:
        print(f"O arquivo {nome} foi criado")


def ler_arq(nome):
    try:
        arq = open(nome, 'rt')
    except FileNotFoundError:
        return
    else:
        sistema.cabecalho("PESSOAS CADASTRADAS")
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<40}{dado[1]:>3} anos')
        arq.close()


def escrever_arq(arq, nome='<desconhecido>', idade=0):
    try:
        a = open(arq, 'at')
    except:
        cprint("Erro ao tentar escrever no arquivo.", 'red')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            cprint('Erro ao tentar gravar os dados.')
        else:
            print(f"Novo registro de {nome} adicionado.")
            a.close()


if __name__ == '__main__':
    pass
