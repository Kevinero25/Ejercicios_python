"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un
descuento del 60%. Escribir un programa que comience leyendo el número de barras
vendidas que no son del día. Después el programa debe mostrar el precio habitual de una
barra de pan, el descuento que se le hace por no ser fresca y el coste final total.
"""

barras = int(input("Número de barras no frescas: "))

precio_normal = 3.49
descuento = 0.60

precio_descuento = precio_normal * (1 - descuento)
total = barras * precio_descuento

print("Precio habitual:", precio_normal)
print("Descuento aplicado:", descuento * 100, "%")
print("Precio final:", total)