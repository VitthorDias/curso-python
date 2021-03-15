from termcolor import colored

print(colored("Digite um número: ",  'magenta'))
num = int(input("--->"))

print("=" * 20)
for p in range(0, 11):
    print(colored(f"{num}*{p} = {num * p}", 'blue'))

print("=" * 20)
