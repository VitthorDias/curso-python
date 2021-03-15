from termcolor import colored

s = 0
c = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        c += 1
        s += i

print(colored(f'A soma de todos os {colored(c, "blue")} é {colored(s, "blue")}.', 'red'))
