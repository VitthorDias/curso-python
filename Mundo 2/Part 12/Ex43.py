from time import sleep

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual a sua altura(no formato x.xx m)? "))
print("\n\033[4mCalculando o seu IMC...\033[m\n")
sleep(2)

imc = peso / pow(altura, 2)
print(f"\033[35mSeu IMC é de {imc:.1f} e sua classificação:\033[0m ", end="")
if imc < 18.5:
    print("\033[1;37mABAIXO DO PESO!")
elif 18.5 <= imc <= 24.9:
    print("\033[1;36mPESO IDEAL!")
elif 25 <= imc <= 29.9:
    print("\033[1;33mSOBREPESO!")
elif 30 <= imc <= 39.9:
    print("\033[1;32mOBESIDADE!")
else:
    print("\033[1;31mOBESIDADE MÓRBIDA!!")
