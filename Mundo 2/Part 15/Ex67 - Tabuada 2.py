while True:
    print("=" * 50)
    num = int(input("Quer ver a tabuada de qual número? "))
    print("=" * 50)
    if num < 0:
        break
    for cont in range(0, 11):
        print(f"{num} X {cont} = {num * cont}")
