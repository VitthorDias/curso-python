sal = float(input("\033[31mSalário do funcionário:\033[m R$"))

print("=" * 50)
if sal > 1250:
    print(f"Novo salário com 10% de aumento:\033[1;32m R${(sal * 1.1):.2f}\033[m!!!")
else:
    print(f'Novo salário com 15% de aumento:\033[1;32m R${(sal * 1.15):.2f}\033[m!!!')
print("=" * 50)
