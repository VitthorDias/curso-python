try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
# except Exception as erro:
#     print(f"Erro encontrado foi {erro.__cause__}.")
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir por zero!")
except KeyboardInterrupt:
    print("O usuário não informou um dado!")
else:
    print(f"O resultado é {r:.1f}")
finally:
    print('Volte sempre!')
