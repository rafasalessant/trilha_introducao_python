# Até 10 anos – R$ 30,00
# Acima de 10 até 29 anos – R$ 60,00
# Acima de 29 até 45 anos – R$ 120,00
# Acima de 45 até 59 anos – R$ 150,00
# Acima de 59 até 65 anos – R$ 250,00
# Maior que 65 anos – R$ 400,00

nome = str(input("Qual o seu nome?"))
idade = int(input("Qual sua idade?"))

if idade <= 10:
    print(f"Olá {nome}, sua idade é {idade} e o valor que será necessário pagar é R$30,00")
elif 11 <= idade <= 29:
    print(f"Olá {nome}, sua idade é {idade} anos e o valor que será necessário pagar é R$60,00")
elif 30 <= idade <= 45:
    print(f"Olá {nome}, sua idade é {idade} anos e o valor que será necessário pagar é R$120,00")
elif 46 <= idade <= 59:
    print(f"Olá {nome}, sua idade é {idade} anos e o valor que será necessário pagar é R$150,00")
elif 60 <= idade <= 65:
    print(f"Olá {nome}, sua idade é {idade} anos e o valor que será necessário pagar é R$250,00")
else:
    print(f"Olá {nome}, sua idade é {idade} anos e o valor que será necessário pagar é R$450,00")
