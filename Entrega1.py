"""
-----------------------------------------------------------------------------------------------
Título: practica clase 05 
Fecha:23-9
Autor:Carbonari Santino

Descripción:

Pendientes:
-----------------------------------------------------------------------------------------------
"""
#----------------------------------------------------------------------------------------------
# MÓDULOS IMPORT
#----------------------------------------------------------------------------------------------
import random 


#----------------------------------------------------------------------------------------------
# FUNCIONES
#----------------------------------------------------------------------------------------------
def separadorAsterisco():
    for i in range(50):
        print("*",end="")
    print()

def generarNumeros(numeros):
    
    
    if len(numeros) > 0:
        respuesta = input("Lista detectada ¿desea remplazarla? (si = 1) (no = 0) ")
        if respuesta == "1": 
            numeros.clear()
            
        else:
            return numeros
    
    cantidad = int(input("¿Cuántos números querés generar? "))
    
    
    for i in range (0,cantidad):
        numero =  random.randint (0,99999)
        numeros.append(numero)
    return numeros
        
def valoresTopN(numeros):
    """
    Identifica y muestra los N valores mayores únicos de una lista.

    Parámetros:
        numeros: Lista de números enteros.

    Retorno:
        Ninguno.
    """

    if len(numeros) == 0:
        print("Primero debe generar los valores.")
        return
    entradaValida = False

    while entradaValida == False:
        entrada = input("Ingrese la cantidad N de valores a mostrar: ")

        if entrada.isdigit():
            n = int(entrada)

            if n > 0:
                entradaValida = True
            else:
                print("N debe ser mayor que cero.")
        else:
            print("Debe ingresar un número entero positivo.")

    ranking = []

    while len(ranking) < n:
        mayor = None

        for numero in numeros:
            if numero not in ranking:
                if mayor is None or numero > mayor:
                    mayor = numero

        if mayor is None:
            break

        ranking.append(mayor)

    print("*******************************************************************************")
    print("VALORES DEL JUEGO DE DATOS (DATOS TOP N)")
    print("*******************************************************************************")

    for i in range(len(ranking)):
        print(i + 1, ". ", ranking[i], sep="")

    print("*******************************************************************************")

    if len(ranking) < n:
        print("Se solicitaron", n, "valores, pero solo existen",
              len(ranking), "valores únicos disponibles.")

#----------------------------------------------------------------------------------------------
# CUERPO PRINCIPAL
#----------------------------------------------------------------------------------------------
def main():
    numeros = []
    separadorAsterisco()
    numeros = generarNumeros(numeros)
    print(numeros)
    valoresTopN(numeros)

main()
