print("Digite a frase para verificar se é palindromo:")
pal = str(input("--> ")).upper().strip().split()
tpal = ''.join(pal)

''' ipal = tpal[::-1]''' #fazendo assim, basta ignorar o "for..."

ipal = ''
print("O que você digitou: ", tpal)

for pl in range(len(tpal) - 1, -1, -1):
    ipal += tpal[pl]

print("O inverso: ", ipal)
if ipal == tpal:
    print("\033[35mÉ palindromo!!!")
else:
    print("\033[35mNão é palindromo!!!")
