#O IMC – Índice de Massa Corporal é um critério da Organização Mundial de Saúde para dar uma indicação sobre a condição de peso de uma pessoa adulta.
#A fórmula é IMC = peso / (altura)²
#Elabore um algoritmo que leia o peso e a altura e imprima o IMC calculado
#Utilizando como base o Desafio 2, complemente o algoritmo informando ao usuário a categoria da pessoa, com base na seguinte tabela:
#IMC em adultos	Condição
#Abaixo de 18,5	Abaixo do peso
#Entre 18,5 e 25	Peso normal
#Entre 25 e 30	Acima do peso
#Acima de 30	Obeso

altura = float(input("Qual sua altura?"))
peso = float(input("Qual seu peso?"))

seu_imc = peso / (altura ** 2)
print(f"Seu IMC é {seu_imc:.2f}")

if seu_imc < 18.5:
    print(f"Você está abaixo do peso")
elif seu_imc >= 18.5 and seu_imc <= 24.9:
    print(f"Você está no peso ideal")
elif 25 <= seu_imc <= 29.9:
    print(f"Você está com sobrepeso")
elif 30 <= seu_imc <= 39.9:
    print(f"Você está com obesidade")
else:
    print(f"Você está com obesidade mórbida")
