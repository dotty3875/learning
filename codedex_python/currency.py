"""We just got home from a fun trip to South America, specifically Colombia, Peru, and Brazil. There's some leftover cash in:

🇨🇴 Colombian pesos
🇵🇪 Peruvian soles
🇧🇷 Brazilian reais
Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD.

Make sure to Google the current exchange rates!"""

pesos = int(input("How much do you have in Columbian pesos?: "))
reais = int(input("How much do you have in Brazillian reais?: "))
soles = int(input("How much do you have in Perivuan soles?: "))

pesos_conversion = pesos / 19.2307
reais_conversion = reais / 5.5555
soles_conversion = soles / 3.703

usd = pesos_conversion + reais_conversion + soles_conversion
print(usd)

