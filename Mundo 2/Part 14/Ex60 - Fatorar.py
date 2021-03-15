n = int(input("Digite um número: "))
c = 1
print(f"{n}! ", end='')
while n > 0:
    print(f"{n} ", end='')
    print('x' if n > 1 else '=', end=' ')
    c *= n
    n -= 1
print(c)
