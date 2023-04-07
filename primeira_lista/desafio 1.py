# massa = pressao * volume / (0.37(temperatura + 460))

pressao = float(input("pressão:"))
volume = float(input("volume:"))
temperatura = float(input("temperatura:"))

massa = pressao * volume / (0.37 * (temperatura + 460.0))

print(f"A massa é: {massa:.2f}")
