# Escreva um algoritmo que leia um número e informe se ele é
# divisível por 10, por 5, por 2 ou se não é divisível por nenhum destes.

numero = int(input("Digite um número inteiro:"))

if numero % 10 == 0:
    print(f"Seu número é divisivel por 10")
else:
    print(f"Seu número não é divisel por 10.")
if numero % 5 == 0:
    print(f"Seu número é divisivel por 5")
else:
    print(f"Seu número não é divisel por 5.")
if numero % 2 == 0:
    print(f"Seu número é divisivel por 2")
else:
    print(f"Seu número não é divisel por 2.")
