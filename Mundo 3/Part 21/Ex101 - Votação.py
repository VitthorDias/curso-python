def voto(idade):
    from datetime import datetime

    idade = datetime.now().year - idade
    if 18 <= idade <= 60:
        return f"Tem {idade} anos. Voto é OBRIGATORIO!"
    elif 16 <= idade < 18 or idade > 60:
        return f"Tem {idade} anos. Voto é OPCIONAL!"
    else:
        return f"Tem {idade} anos. Voto NEGADO!"


# Função Principal
ano = int(input("Em que ano você nasceu? ").strip())
print(voto(ano))
