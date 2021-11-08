#***********************************************************
# Fecha: 06/11/2021
# Autor: Aldana Vallejos
# Guia N8
#***********************************************************
# EJERCICIO 3: Se pide que defina el procedimiento CaballoRojoCapturarPosición1() que permita realizar
#              el movimiento del caballo hacia la posición 1 de la figura y capturar una pieza rival si existe. Para esto considere que: 
#              ● El movimiento característico del “Caballo” es en forma de una L de 2x3 o 3x2 casilleros (contando el casillero de partida). 
#              ● El caballo además tiene la cualidad (única entre todas las piezas) de poder “saltar” piezas, de forma que puede pasar
#              a través de casilleros donde exista una pieza para llegar a su destino. 
#              ● Para que el caballo rojo pueda capturar una pieza rival en la posición 1, debe existir en la posición 1 una ficha rival.
#              ● En este caso el caballo rojo toma el lugar de la pieza rival (la pieza rival es removida del tablero y el caballo
#              queda en el lugar donde estaba la pieza rival). 
#              ● En caso contrario, o sea si no hay pieza rival en la posición 1, el caballo no realiza ningún movimiento (se queda en el lugar de partida).
#              ● Además debe tener en cuenta que si el caballo toma una pieza rival, el casillero de partida debe quedar
#              sin ninguna pieza, es decir se debe corresponder con un tablero vacío de ajedrez (en donde un casillero puede ser blanco o negro)

#***********************************************************
#                    D I S E Ñ O
#***********************************************************
#Declaracion de variables
def CaballoRojoCapturarPosicion1(): #defino la función
    import random
    rival=["Si","No"]
    #constantes
    filas=5
    columnas=5
    tablero=[[0,3,0,2,0],[4,0,0,0,1],[0,0,"C",0,0],[5,0,0,0,8],[0,6,0,7,0]]
    #los 0 representan los casilleros vacios.

    print() 
    for f in range(filas): #armo la matriz
        for c in range(columnas):
            print(tablero[f][c], end=" ")
        print()
    print()

    if random.choice(rival)=="Si": #Caso de que exista pieza rival
        print("Hay una pieza rival en la posición 1. El caballo captura dicha pieza y permanece en el nuevo lugar tomado.")
        tablero=[[0,3,0,2,0],[4,0,0,0,"C"],[0,0,0,0,0],[5,0,0,0,8],[0,6,0,7,0]] #modifico la matriz
        print() 
        for f in range(filas): #armo la matriz
            for c in range(columnas):
                print(tablero[f][c], end=" ")
            print()
        print()
    elif random.choice(rival)=="No": #Caso de que no exista pieza rival
        print("NO hay una pieza rival en la posición 1. El caballo no realiza ningún movimiento.")
        tablero=[[0,3,0,2,0],[4,0,0,0,1],[0,0,"C",0,0],[5,0,0,0,8],[0,6,0,7,0]] #modifico la matriz
        print() 
        for f in range(filas): #armo la matriz
            for c in range(columnas):
                print(tablero[f][c], end=" ")
            print()
        print()

CaballoRojoCapturarPosicion1() #Llamo a la función