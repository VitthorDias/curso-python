from time import sleep


def maior(* num):
    print("==" * 30)
    print("Analisando os valores passados...")
    sleep(1)
    for k, v in enumerate(num):
        print(v, end=' ')
        sleep(0.4)
    print(f' Foram informados {len(num)} valores ao todo.')
    if len(num) == 0:
        maio = 0
    else:
        maio = max(num)
    print(f'O maior valor informado foi {maio}')


# Função Principal
maior(7, 8, 4, 0, 6, 2)
maior(4, 0, 10)
maior()
maior(20, 4, 0, 8)
