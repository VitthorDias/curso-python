def soma(* val):
    s = 0
    for n in val:
        s += n
    print(f'Somando os {val} temos {s}.')
    print(f'A soma {sum(val)}')


soma(4, 2)
soma(5, 2, 4)
