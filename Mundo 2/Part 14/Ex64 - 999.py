n = s = c = 0
n = int(input("Digite um número arquivo: "))
while n != 999:
    s += n
    c += 1
    n = int(input("Digite um número arquivo: "))
print(f"\nVocê digitou {c} números e a soma entre eles é {s}.")
