n = int(input("Quantos elementos? "))
n1 = c = 0
n2 = 1
s = n1 + n2

while c < n:
    print(f"{n1}", end=". ")
    n1 = n2
    n2 = s
    s = n1 + n2
    c += 1
