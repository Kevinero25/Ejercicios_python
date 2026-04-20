"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión.
"""

cantidad = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual (%): "))
años = int(input("Años: "))

capital = cantidad * (1 + interes / 100) ** años

print("Capital obtenido:", capital)