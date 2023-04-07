# Construa um algoritmo que leia um número e, se ele for maior do que 20, então imprima a metade do número.

numero = int(input("Insira um número inteiro:"))

if numero > 20:
    print(f"Seu número é maior do que 20 e a sua metade é: {numero / 2}")
elif numero == 20:
    print(f"Seu número é igual a 20")
else:
    print(f"Seu número é menor do que 20")
