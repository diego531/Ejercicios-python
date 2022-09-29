

menu = """
Bienvenido al conversor de monedas 🤙

1 - Pesos colombianos a dolares
2 - Pesos argentinos a dolares
3 - Pesos argentinos a dolares
4 - Dolares a pesos colombianos

Elige una opcion : """

opcion = input(menu)

if opcion == "1":
    pesos = input("¿cuantos pesos colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == "2":
    pesos = input("¿cuantos pesos argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == "3":
    pesos = input("¿cuantos pesos mexicanos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 24
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")
elif opcion == "4":
    dolares = input ("¿Cuantos dolares tienes?: ")
    dolares = float(dolares)
    valor_peso = 0.00022
    pesos = dolares / valor_peso
    pesos = round(pesos , 2)
    pesos = str(pesos)
    print("Tienes $" + pesos + " Pesos Colombianos")
else:
    print("Ingresa una opción correcta please")


# Pesos colombianos a dolares


# #Dolares a pesos colombianos


