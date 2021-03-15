from time import sleep
num1 = int(input("Digite um número arquivo: "))
num2 = int(input("Digite outro número arquivo: "))
print("\033[1;31mProcessando...\033[m\n")

sleep(2)
print('#¨'*20)
if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print("Os dois números são iguais.")
print('#¨'*20)
