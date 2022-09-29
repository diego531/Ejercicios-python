
def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos) 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " Dolares")


menu = """
Bienvenido al conversor de monedas 🤙

1 - Pesos colombianos a dolares
2 - Pesos argentinos a dolares
3 - Pesos mexicanos a dolares

Elige una opcion : """

opcion = input(menu)

if opcion == "1":
    conversor("Colombianos", 3875)
elif opcion == "2":
    conversor("Argentinos", 65)
elif opcion == "3":
    conversor("Mexicanos", 24) 
else:
    print("Ingresa una opción correcta please")



