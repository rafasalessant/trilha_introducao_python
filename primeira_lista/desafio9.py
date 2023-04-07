# Ler um número e imprimir se ele é igual a 5, 200, a 400, se está no intervalo entre 500 e 1000,
# inclusive, ou se ele está fora dos escopos anteriores.

numero = int(input("Insira o número para comparação:"))

if numero == 5:
    print(f"Seu número é igual a 5")
elif numero == 200:
    print(f"Seu número é igual a 200")
elif numero == 400:
    print(f"Seu número é igual a 400")
elif 500 <= numero <= 1000:
    print(f"Seu número está entre 500 e 1000")
else:
    print(f"Seu número não se encaixa nas comparações")
