"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el
método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un
método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
"""


class Calculadora:
    def __init__(self):
            self.__num1 = int(input("Introduce el primer numero!: "))
            self.__num2 = int(input("Introduce el segundo valor!: "))
    

    def suma(self):
        suma=self.__num1+self.__num2
        print("La suma es: ",suma)

    def resta(self):
        resta=self.__num1-self.__num2
        print("La resta es: ",resta)

    def multiplicar(self):
        multiplicar=self.__num1*self.__num2
        print("La multiplicacion es: ",multiplicar)

    def dividir(self):
        dividir= self.__num1/self.__num2
        print("La division es: ",dividir)


    def imprimir(self):
        print("Las respuestas de todas las operaciones son: ")
        print("num1: ",self.__num1)
        print("num2 :",self.__num2)