num = int(input("Digite o número arquivo a ser convertido: "))
print(f"Escolha uma das opções para converter o número {num}")
print("""\033[31m1->\033[m BINÁRIO.\n\033[31m2->\033[m OCTAL.\n\033[31m3->\033[m HEXADECIMAL.""")
base = int(input("---> "))

cr = {'a': '\033[1;31m', 'b': '\033[1;36m', 'clear': '\033[m'}
print("-#-"*20)
if base == 1:
    print(f"{cr['a']}{num}{cr['clear']} convertido para BINÁRIO é {cr['b']}{bin(num)[2:]}{cr['clear']}.")
elif base == 2:
    print(f"{cr['a']}{num}{cr['clear']} convertido para OCTAL é {cr['b']}{oct(num)[2:]}{cr['clear']}")
else:
    print(f"{cr['a']}{num}{cr['clear']} convertido para HEXADECIMAL é {cr['b']}{hex(num)[2:].upper()}{cr['clear']}")
print("-#-"*20)
