from math import hypot
c1 = float(input("Tamanho do cateto adjacente:"))
c2 = float(input("Tamanho do cateto oposto:"))
print(f'O valor da hipotenusa é {(hypot(c1 , c2)):.3f}')
