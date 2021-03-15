sexo = str(input("Digite o sexo M/F: ").upper().strip()[0])
while sexo not in "MF":
    sexo = str(input("\033[31mSexo digitado incorretamente. Digita novamente.\033[m\n")).upper().strip()[0]
print("\n\033[35mVocê digitou corretamente.")
