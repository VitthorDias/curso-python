def dobra(lst):
    pos = 0
    while pos < len(valores):
        lst[pos] *= 2
        pos += 1


valores = [7, 0, 4, 6, 2, 9]
dobra(valores)
print(valores)
