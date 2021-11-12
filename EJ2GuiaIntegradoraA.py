#***********************************************************
# Fecha: 24/10/2021
# Autor: Aldana Vallejos
# Guia N7
#***********************************************************
# EJERCICIO 2: Suponiendo que el primer día del año fue lunes, escribir una función que reciba 
# un número con el día del año (de 1 a 366) y devuelva el día de la semana que le toca. 
# Por ejemplo: si recibe '3' debe devolver 'miércoles', si recibe '9' debe devolver 'martes'
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
dia=0
resto=0
entero=0
diasdelaño=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

def diadelasemana (dia): #Creo la función
    resto=dia%7
    if resto==1:
        print(diasdelaño[0]) #Salidas por pantalla
    else:
        if resto==2:
            print(diasdelaño[1])
        else:
            if resto==3:
                print(diasdelaño[2])
            else:
                if resto==4:
                    print(diasdelaño[3])
                else:
                    if resto==5:
                        print(diasdelaño[4])
                    else:
                        if resto==6:
                            print(diasdelaño[5])
    if resto==0:
        entero=dia//7
        print(diasdelaño[6])

# Ingreso de dato
while dia<=0 or dia>366: #Validaciones
    try:
        dia=int(input("Ingrese el número del día (desde 1 hasta 366): "))
        if dia<=0 or dia>366:
            print("Error. Ingrese un numero mayor a 1 y menor que 366")
        else:
            diadelasemana(dia) #Ejecuto la función
            break
    except ValueError:
        print("Error. Ingrese un numero mayor a 1 y menor que 366")