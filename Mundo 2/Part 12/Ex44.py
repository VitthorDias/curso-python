cr = {'v': '\033[1:31m', 'mg': '\033[1;35m', 'cl': '\033[m'}
price = float(input("Preço normal do produto: "))
print("Escola a forma de pagamento")

# Lista das formas de pagamento.
print("""\n{}1 -{} À vista no dinheiro/chegue (-10%).\n{}2 -{} À  vista no cartão (-5%).
{}3 -{} Até 2x no cartão (normal).\n{}4 -{} 3x ou mais (+20%)."""
      .format(cr['v'], cr['cl'], cr['v'], cr['cl'], cr['v'], cr['cl'], cr['v'], cr['cl']))
#Fim da lista.
pay = int(input("---> "))

if pay == 1:
    print(f"{cr['mg']}Valor a pagar é de \033[1;36mR${(price * 0.9):.2f}")
elif pay == 2:
    print(f"{cr['mg']}Valor a pagar é de \033[1;36mR${(price * 0.95):.2f}")
elif pay == 3:
    print(f"{cr['mg']}Valor a pagar é de \033[1;36mR${(price):.2f}")
elif pay == 4:
    parc = int(input("Quantas parcelas? "))
    valor = price * 1.2
    print(f"""{cr['mg']}Valor a pagar será de {parc}X de \033[1;36mR${(valor / parc):.2f}{cr['mg']},
valor total de \033[1;36mR${(valor):.2f}.""")
else:
    print("Opção inválida!!!")
