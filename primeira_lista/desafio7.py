# Desenvolva um algoritmo que leia três números e armazene o maior número na variável de nome MAIOR
primeiro_numero = int(input("Digite o primeiro número:"))
segundo_numero = int(input("Digite o segundo número:"))
terceiro_numero = int(input("Digite o terceiro número:"))

if primeiro_numero > segundo_numero and primeiro_numero > terceiro_numero:
    MAIOR = primeiro_numero
elif segundo_numero > primeiro_numero and segundo_numero > terceiro_numero:
    MAIOR = segundo_numero
else:
    MAIOR = terceiro_numero

print(f"O maior número é {MAIOR=}")
