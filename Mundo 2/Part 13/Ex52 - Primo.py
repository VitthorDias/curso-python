from termcolor import colored

num = int(input("\033[35mDigite um número para verificar se é primo: "))

s = 0
for i in range(1, num + 1):
    if num % i == 0:
        print(colored(i, 'blue'), end=' ')
        s += 1
    else:
        print(colored(i, 'red'), end=" ")

if s == 2:
    print(f"\n\n\033[36mO número {num} é PRIMO!!!")
else:
    print(f"\n\n\033[36mO número {num} NÃO é primo!!!")
