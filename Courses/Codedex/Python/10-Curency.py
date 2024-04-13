print("What is the value in USD of the currencies you bring back from South America?\n")

pesos = int(input("What do you have left in pesos ? "))
soles = int(input("What do you have left in soles ? "))
reais = int(input("What do you have left in reais ? "))

# Exchange rates 2024-04-08
pesos_rate = 0.061
soles_rate = 0.27
reais_rate = 0.20
pesos_value = pesos * pesos_rate
soles_value = soles * soles_rate
reais_value = reais * reais_rate
total_value = pesos_value + soles_value + reais_value
print("***************************************************")
print(f"{pesos} pesos x {pesos_rate} = {pesos_value} USD")
print(f"{soles} soles x {soles_rate} = {soles_value} USD")
print(f"{pesos} pesos x {reais_rate} = {reais_rate} USD")
print("***************************************************")
print(f"The total value of your trip leftovers is: {total_value} USD")
print("***************************************************")
