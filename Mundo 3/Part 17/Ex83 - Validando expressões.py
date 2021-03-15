expr = str(input("Digite a expressão: "))
par = []
for qtd in expr:

    if qtd == '(':
        par.append('(')
    elif qtd == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')

if len(par) == 0:
    print("Expressão valida!!!")
else:
    print("Expressão invalida!!!")
