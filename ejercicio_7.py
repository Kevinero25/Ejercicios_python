"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el
índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu
índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
redondeado con dos decimales.
Cálculo de imc:consiste en dividir el peso, expresado en kilos, entre la estatura, en metros,
elevada al cuadrado (kg/m2)
"""

Bienvenida=input("Vamos a medir tu imc! quieres continuar? s/n: ")

if Bienvenida == "s":
    print("Listo entonces empezemos!")
else:
    print("Como que no? >:V")
    exit()

peso=float(input("Cuanto pesas?:  "))
altura=float(input("Cuanto mides?: "))

imc = peso/(altura** 2)

print(f"Perfecto tu IMC es: {imc: .2f}")
