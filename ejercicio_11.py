"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al
año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la
cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después
el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer,
segundo y tercer años. Redondear cada cantidad a dos decimales.
"""

cantidad = float(input("Cantidad depositada: "))

año1 = round(cantidad * 1.04, 2)
año2 = round(año1 * 1.04, 2)
año3 = round(año2 * 1.04, 2)

print("Año 1:", año1)
print("Año 2:", año2)
print("Año 3:", año3)