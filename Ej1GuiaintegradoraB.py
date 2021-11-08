#***********************************************************
# Fecha: 03/11/2021
# Autor: Aldana Vallejos
# Guia N8
#***********************************************************
# EJERCICIO 1: Se desarrolla una carrera automovilística de regularidad constituida por 50 trayectos
#              numerados de 1 a 50. Por cada trayecto se registra  el número de trayecto y el tiempo
#              asignado en segundos y se encuentran en el archivo ASIGNADO (sin ningún orden)
#              a) Nro. del trayecto	
#              b) Tiempo asignado en segundos (4 dígitos)
#              Para llevar el control de los corredores, de posición y de abandonos se dispone de un archivo TIEMPO donde cada registro contiene:
#              a) Nro. del corredor (3 dígitos)
#              b) Nro. del trayecto
#              c) Tiempo en segundos (4 dígitos)
# 
#              El lote esta ordenado por trayecto pero no por corredor. A partir del abandono de un corredor
#              en un trayecto no habrá más ingresos en el lote.
#              Desarrollar estrategia, algoritmo y codificación del programa que determine e imprima:
#              1) Por cada etapa, su número y el del corredor ganador de la misma.
#              2) Por cada etapa, su número y los de los corredores que abandonan en la misma.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
#Declaracion de variables
#constante
trayectos=50

tiempo_asig=0
nro_corredor=0
nro_trayecto=0
tiempo_seg=0
abandono=""
minimo=10000
ganador=0
abandonos=[]
terminar="no"
#Archivos
asignado=[]
tiempo=[]

def resultados1 (abandonos,ganador,minimo): #Defino la función
    print()
    #Salidas por pantalla
    print("El número del corredor ganador es: {0} con {1} segundos".format(ganador,minimo))
    print("Los números de los corredores que abandonaron por cada etapa son: {0}".format(abandonos))

for i in range(1,trayectos+1): #lotes
    try:
        tiempo_asig=int(input(f"Ingrese el tiempo asignado en segundos (4 digitos) del trayecto {i}: ")) #Ingreso de dato
        asignado.append(i)
        asignado.append(tiempo_asig)
    except ValueError: #Validación
        print("Error. Ingrese números")
        terminar="si"
        break

while terminar=="no":
      for x in range(1,trayectos+1):
        try:
          nro_corredor=int(input(f"Ingrese el número del corredor (3 digitos) del trayecto {x}: ")) #Ingreso de dato
          tiempo.append(nro_corredor)
        except ValueError: #Validación
          print("Error. Debe ingresar números.")
          terminar="si"
          break

        abandono=input("El corredor abandonó el trayecto? esciba 'si' o 'no' a continuación: ") #Ingreso de dato
        match abandono:
            case "si":
                abandonos.append(x)
                abandonos.append(nro_corredor) #lista de corredores que abandonaron
            case "no":
                tiempo_seg=int(input("Ingrese el tiempo en segundos (4 digitos): ")) #Ingreso de dato
                if tiempo_seg<=0:
                    print("Error. Ingrese un valor válido.") #Validación
                elif tiempo_seg>0:
                    tiempo.append(tiempo_seg)
                    if tiempo_seg<minimo:
                        minimo=tiempo_seg
                        ganador=nro_corredor #corredor que ganó 
            case _: #Validación
                print("Error. El caracter ingresado no es correcto.")
      resultados1(abandonos,ganador,minimo) #Llamo a la función
      terminar="si"
      break