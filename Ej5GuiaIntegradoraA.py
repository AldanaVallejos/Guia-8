#***********************************************************
# Fecha: 27/10/2021
# Autor: Aldana Vallejos
# Guia N7
#***********************************************************
# EJERCICIO 5: Se pide que implemente el procedimiento ReparandoLaNave(). Teniendo en cuenta que el marciano
# de la imagen debe llegar a su hogar con suficiente combustible, se pide que recorra el camino indicado, teniendo
# en cuenta que en el medio se puede encontrar con combustible, el cual, es representados por celdas Rojas y Negras.
# El combustible podría estar en cualquier parte del camino. Si el combustible es Rojo, nuestro amigo el marciano se
# detendrá y dejará una mancha Verde en el lugar, debido a que encontró combustible de calidad, pero luego seguirá su
# camino. Si el combustible es Negro, podrá avanzar sin problemas. El camino tiene 5 celdas de ancho.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
def ReparandoLaNave():
    #constantes
    filas=7
    columnas=5
    camino=[[2,0,1,0,2],[0,0,0,0,0],[2,1,0,2,1],[0,0,0,0,0],[1,0,2,0,1],[0,0,0,0,0],[2,0,2,0,1]]
    #los 2 representan a los combustibles rojos, los 1 representan a los combustibles negros y los 0 representan a las celdas blancas.

    print() 
    for f in range(filas): #armo la matriz
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print()

    print("El marciano comienza su camino...")
    print()
    camino=[[2,0,1,0,2],[0,0,0,0,0],[2,1,0,2,1],[0,0,0,0,0],[1,0,2,0,1],[0,0,0,0,0],[3,0,2,0,1]] #los 3 representan a las manchas verdes
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano se detiene. deja una mancha verde debido al combustible rojo y sigue avanzando.")
    print()

    camino=[[2,0,1,0,2],[0,0,0,0,0],[2,1,0,2,1],[0,0,0,0,0],[1,0,2,0,1],[0,0,0,0,0],[3,0,3,0,1]]
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano se detiene. deja una mancha verde debido al combustible rojo y sigue avanzando.")
    print()

    camino=[[2,0,1,0,2],[0,0,0,0,0],[2,1,0,2,1],[0,0,0,0,0],[1,0,3,0,1],[0,0,0,0,0],[3,0,3,0,1]]
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano se detiene. deja una mancha verde debido al combustible rojo y sigue avanzando.")
    print()

    camino=[[2,0,1,0,2],[0,0,0,0,0],[2,1,0,3,1],[0,0,0,0,0],[1,0,3,0,1],[0,0,0,0,0],[3,0,3,0,1]]
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano se detiene. deja una mancha verde debido al combustible rojo y sigue avanzando.")
    print()

    camino=[[2,0,1,0,2],[0,0,0,0,0],[3,1,0,3,1],[0,0,0,0,0],[1,0,3,0,1],[0,0,0,0,0],[3,0,3,0,1]]
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano se detiene. deja una mancha verde debido al combustible rojo y sigue avanzando.")
    print()

    camino=[[2,0,1,0,3],[0,0,0,0,0],[3,1,0,3,1],[0,0,0,0,0],[1,0,3,0,1],[0,0,0,0,0],[3,0,3,0,1]]
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano se detiene. deja una mancha verde debido al combustible rojo y sigue avanzando.")
    print()

    camino=[[3,0,1,0,3],[0,0,0,0,0],[3,1,0,3,1],[0,0,0,0,0],[1,0,3,0,1],[0,0,0,0,0],[3,0,3,0,1]]
    for f in range(filas):
        for c in range(columnas):
            print(camino[f][c], end=" ")
        print()
    print("El marciano llegó a su destino.")
    
ReparandoLaNave()