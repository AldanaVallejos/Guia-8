#***********************************************************
# Fecha: 27/10/2021
# Autor: Aldana Vallejos
# Guia N7
#***********************************************************
# EJERCICIO 4: Se quiere generar el código de programación necesario para realizar la afinación de un piano.
# Para esto, el afinador posee un dispositivo que escucha la nota de cada tecla, la compara con una nota esperada,
# e indica si es correcta o no. La nota escuchada en el piano será correcta si la celda que la representa tiene el
# mismo color que la celda que representa la nota esperada. Hay dos tipos de teclas, blancas y negras, por lo que hay
# dos formas de representar la nota, con una celda blanca (vacía) o negra. En el caso contrario, el dispositivo indicará
# que la nota del piano debe afinarse y esto se representará marcando la nota mediante una celda de color Rojo. La siguiente
# imagen muestra un ejemplo antes y después de la verificación donde: 
#      ● Cada columna representa una tecla o nota del piano. 
#      ● Solo se representan las primeras 12 teclas del piano. 
#      ● La primer tecla (de izquierda a derecha) está afinada pues ambas notas son de color negro. 
#      ● La cuarta tecla también está afinada, pues ambas son de color blanco. 
#      ● La segunda tecla está desafinada, pues la nota del piano escuchada es de color negro, y 
# la esperada es de color blanco. Se le pide que implemente el procedimiento VerificarAfinacionDePiano() 
# que indica con un casillero rojo aquellas teclas del piano que deben afinarse, para un piano de 88 teclas. 
# Antes de llamar al procedimiento Luego de llamar al procedimiento
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Constantes
fila=1
columnas=88
# Declaracion de variables
notas_afinadas=[]
import random

print()
print("Nota piano")
notas_escuchadas=[[random.randint(0,1)]for _ in range (88)] #los ceros representan las teclas blancas y los 1 las teclas negras
print(notas_escuchadas, end=" ") #Salida por pantalla
print()

print("Nota esperada")
notas_esperadas=[[random.randint(0,1)]for _ in range (88)] #los ceros representa las teclas blancas y los unos las teclas negras
print(notas_esperadas, end=" ") #Salida por pantalla
print()

def VerificarAfinacionDePiano(): #Defino la función
    print()
    print("¿Debe afinarse?")
    for x in range(0,columnas):
        nota=notas_escuchadas[x]
        esperada=notas_esperadas[x]
        if nota!=esperada:
            notas_afinadas.append("rojo") #Caso de que se requiera afinar la tecla
        else:
            notas_afinadas.append(" ") #Caso de que no se requiera afinar la tecla
    print(notas_afinadas) #Salida por pantalla
    print()

print()
llamar=input("Si desea llamar al procedimiento escriba SI: ") #Salida por pantalla
if llamar.upper()=="SI":
    VerificarAfinacionDePiano() #Llamo a la función
else:
    print("Finaliza.") 