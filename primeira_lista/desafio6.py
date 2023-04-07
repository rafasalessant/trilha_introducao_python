# Criar um algoritmo que leia dois números e imprima uma mensagem dizendo se são iguais ou diferentes.

primeiro_numero = int(input("Insira o primeiro número para comparação:"))
segundo_numero = int(input("Insira o segundo número para comparação:"))

if primeiro_numero == segundo_numero:
    print(f"{primeiro_numero} e {segundo_numero} são iguais")
else:
    print(f"{primeiro_numero} e {segundo_numero} são diferentes")
