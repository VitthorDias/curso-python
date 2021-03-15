from lib import sistema, arquivo
from time import sleep

while True:
    aq = arquivo.ver_arq('cursopython')
    if not aq:
        arquivo.criar_arq('cursopython')
    else:
        opc = ['Ver pessoas cadastrada.', 'Cadastrar novas pessoas.', 'Sair do sistema']
        resp = sistema.menu(opc)

        if resp == 1:
            arquivo.ler_arq('cursopython')
        if resp == 2:
            sistema.dados()
        if resp == 3:
            sistema.cabecalho("Saindo do sistema..")
            break
        sleep(2)
