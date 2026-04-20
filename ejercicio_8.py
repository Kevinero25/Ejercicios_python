"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla “La
división de <n> entre <m> da un cociente <c> y un resto <r>” donde <n> y <m> son los
números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la división
entera respectivamente.
"""

operacion = print("Dame dos numeros enteros y haremos una division con todo el resultado!!")
n=int(input("Vamos con el primer numero: "))
m=int(input("Vamos con el segundo numero: "))


cociente = n // m
resto = n % m

print(f"Y la respuesta es!!  {cociente} y el resto es {resto: .2f}")