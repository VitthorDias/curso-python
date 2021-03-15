from time import sleep
from random import randint

print("=========")
print("JO KEN PO")
print("=========")
sleep(1)
print("Vamos jogar :)")
sleep(0.6)
print("Mas antes, deixe eu te pergunta uma coisa. Você sabe jogar JOKENPO?")
print("1 - SIM \n2 - NÃO")
perg = int(input("---> "))

#Explicando como funciona o jogo.
if perg == 2:
    print("\n\n->Ok. vou lhe ensinar então")
    sleep(1)
    print("""->Nesse jogo você e o seu oponente vai escolher entre 'pedra, papel e tesoura', no entanto, se fala
o nome do jogo pausadamente antes de revelarem suas decisões. A seguir você verá quem ganha..""")
    sleep(5)
    print("\n->Ganha do lado direito e Perdeu do lado esquerdo")
    print("Pedra - Tesoura \nTesoura - Papel \nPapel - Pedra")
    sleep(3)
    print("->E é isso. Agora vamos jogar :)\n\n")
    sleep(3)

#Escolhas
print("->Enquanto você escolhe o seu, eu escolherei o meu.")
print("0 - Pedra \n1 - Papel \n2 - Tesoura")
player = int(input("---> "))
pc = randint(0, 2)
op = ('Pedra', 'Papel', 'Tesoura')

#Falando JO KEN PO
sleep(0.2)
print("JO  ", end="")
sleep(0.8)
print("KEN  ", end="")
sleep(0.8)
print("PO\n")

#Analisando
print(f'Você escolheu {op[player]} e eu escolhi {op[pc]}.')
if player == 0 and pc == 2:
    print('Parabéns. Você GANHOU!!!')
elif player == 1 and pc == 0:
    print('Parabéns. Você GANHOU!!!')
elif player == 2 and pc == 1:
    print('Parabéns. Você GANHOU!!!')
elif player == pc:
    print(('EMPATAMOS xD!!!'))
else:
    print("Você PERDEU!!!")
