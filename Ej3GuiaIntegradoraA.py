#***********************************************************
# Fecha: 22/10/2021
# Autor: Aldana Vallejos
# Guia N7
#***********************************************************
# EJERCICIO 3: Escribir un programa que le pida al usuario que ingrese una sucesión de números naturales (primero uno,
# luego otro, y así hasta que el usuario ingrese ’-1’ como condición de salida). Al final, el programa debe imprimir
# cuántos números fueron ingresados, la suma total de los valores y el promedio.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
nro=0

def numerossumapromedio(nro): #Defino la función
    numerosnaturales=[] #Lista que va a contener los numeros naturales que se ingresen
    contador=0
    sumatotal=0
    while nro<-1 or nro>=0:
        try: #Validación
            nro=int(input("Ingrese una sucesión de números naturales (finaliza con -1): ")) #Ingreso de dato
            if nro<-1: #Validación
                print("Error. Si desea terminar ingrese -1. Si desea ingresar numeros, ingrese únicamente números positivos.") 
            elif nro>=0: 
                contador=contador+1
                numerosnaturales.append(nro)
            elif nro==-1: #Caso de finalizar e imprimir los resultados
                resultados(contador,numerosnaturales) #Llamo a la función
        except ValueError:
            print("Error. Ingrese números")

def resultados(contador,numerosnaturales): #Defino función para los resultados obtenidos
    sumatotal=sum(numerosnaturales)
    promedio=sumatotal/contador
    #Salidas por pantalla
    print("Los números ingresaros fueron {0}".format(numerosnaturales))
    print("La suma total de los valores es {0}".format(sumatotal))
    print("El promedio es {0}".format((round(promedio,2))))

numerossumapromedio(nro) #Llamo a la función