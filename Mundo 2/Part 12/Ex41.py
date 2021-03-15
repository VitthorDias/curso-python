from datetime import date
from time import sleep

ano = int(input("Ano de nascimento do atleta: "))
print("\033[4;31mVerificando categoria...\n\033[m")
sleep(2)

atl = date.today().year - ano
print(f"O atleta possui {atl} anos.")
if atl <= 9:
    print("Categoria do atleta: \033[34mMIRIM\033[m.")
elif atl <= 14:
    print("Categoria do atleta: \033[34mINFANTIL\033[m.")
elif atl <= 19:
    print("Categoria do atleta: \033[34mJUNIOR\033[m.")
elif atl <= 25:
    print("Categoria do atleta: \033[34mSÊNIOR\033[m.")
else:
    print("Categoria do atleta: \033[34mMASTER\033[m.")
