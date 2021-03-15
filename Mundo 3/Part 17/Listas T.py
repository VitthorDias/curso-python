num = [5, 6, 8, 1, 6, 10]
print("-" * 20)
print(num)

num[2] = 0
print("-" * 20)
print(num)

num.append(3)
print("-" * 20)
print(num)

num.sort()
print("-" * 20)
print(num)

num.sort(reverse=True)
print("-" * 20)
print(num)

num.insert(2, 10)
print("-" * 20)
print(num)

num.pop()
print("-" * 20)
print(num)

num.pop(1)
print("-" * 20)
print(num)

num.remove(5)
print("-" * 20)
print(num)

print("-" * 20)
for c, v in enumerate(num):
    print(f"Na posição {c} o valor é {v}!!!")
