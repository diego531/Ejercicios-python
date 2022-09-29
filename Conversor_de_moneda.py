
#Pesos colombianos a dolares

pesos = input("¿cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
valor_dolar = 3875
dolares = pesos / valor_dolar
dolares = round(dolares , 2)
dolares = str(dolares)
print("Tienes $" + dolares + " Dolares")

#Dolares a pesos colombianos

dolares = input ("¿Cuantos dolares tienes?: ")
dolares = float(dolares)
valor_peso = 0.00022
pesos = dolares / valor_peso
pesos = round(pesos , 2)
pesos = str(pesos)
print("Tienes $" + pesos + " Pesos Colombianos")