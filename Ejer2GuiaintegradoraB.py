#***********************************************************
# Fecha: 04/11/2021
# Autor: Aldana Vallejos
# Guia N8
#***********************************************************
# EJERCICIO 2: Una empresa que distribuye mercadería hacia distintas localidades del interior. dispone de dos lotes: Uno denominado DESTINOS
#              con información de la distancia a cada uno de los destinos:
#              a) Nro. de destino (3 dígitos)	
#              b) Distancia en kilómetros (NNN.NNN)
#              
#              Otro denominado VIAJES con los viajes realizados por cada camión (< 200), donde cada registro contiene:
#              a) Patente del camión (6 caracteres)	
#              b) Nro. de destino	
#              c) Nro. de chofer (1 a 150)
# 
#              Desarrollar estrategia, algoritmo y codificación del programa que determine e imprima:
#              1) Cantidad de viajes realizados a cada destino (solo si > 0).  contador en nro_destino_viajes
#              2) Nro. de chofer con menor cantidad de Km (entre los que viajaron). 
#              3) Patente de los camiones que viajaron al destino 116 sin repeticiones de las mismas.
#***********************************************************
#                    D I S E Ñ O
#***********************************************************
#Declaracion de variables
#lotes
destinos=[]
viajes=[]

nro_destino=[]
kilometros=[]
patentes=[]
distanciakm=0.00
seguir="si"
nrodestino=0
ndestino=0
nchofer=0
contador=0
chofermenorkm=0
minimo=11111111111111

def resultados(patentes,contador,chofermenorkm): #Defino la función
    print()
    #salidas por pantalla
    print("La cantidad de viajes realizados a cada destino (>0) son: {0}".format(contador))
    print("El nro de chofer con menor cantidad de km es {0}".format(chofermenorkm))
    if (len(patentes))==0: #caso de que ningún camión haya viajado al destino 116
        print("No hay camiones que viajaron al destino 116, y por lo tanto no hay patentes")
    elif (len(patentes))>0: 
        print("La/s patente/s de el/los camion/es que viajaron al destino 116 es/son: {0}".format(list(set(patentes))))

while True:
    #lote 1
    try:
        print()
        nrodestino=int(input("Ingrese el numero de destino (3 digitos): ")) #Ingreso de dato
        destinos.append(nrodestino)
    except ValueError: #Validación
        print("Error. Ingrese números")
        break
    try:
        distanciakm=float(input("Ingrese la distancia en kilómetros (NNN.NNN): ")) #Ingreso de dato
        destinos.append(distanciakm)
    except ValueError: #Validación
        print("Error. Debe ingresar números")
        break
    #lote2
    patentecamion=input("Ingrese la patente del camión (6 caracteres): ") #Ingreso de dato
    viajes.append(patentecamion)
    try:
        ndestino=int(input("Ingrese el numero de destino: ")) #Ingreso de dato
        viajes.append(ndestino)
    except ValueError: #Validación
        print("Error. Ingrese números")
        break
    if ndestino>0:
        contador=contador+1 #1) Cantidad de viajes realizados a cada destino (solo si > 0)
    
    if ndestino==116: # Patente de los camiones que viajaron al destino 116 sin repeticiones de las mismas.
        patentes.append(patentecamion)
    
    nchofer=int(input("Ingrese el numero de chofer (1 a 150): ")) #Ingreso de dato
    viajes.append(nchofer)
    if nchofer<1 or nchofer>150: #Validación
        print("Error. Está ingresando un número menor a 1 o mayor a 150.")
    if nchofer>=1 and nchofer<150:
        if distanciakm<minimo: #2) Nro. de chofer con menor cantidad de Km (entre los que viajaron). 
            minimo=distanciakm
            chofermenorkm=nchofer

    if nrodestino>0:
        print()
        seguir=input("Desea seguir cargando registros? escriba a continuación 'si' o 'no': ") #Ingreso de dato
        if seguir.lower()!="si" and seguir.lower()!="no": #Validación
                print("Error. Ingrese un caracter válido.")
        elif seguir=="no":
            resultados(patentes,contador,chofermenorkm) #Llamo a la función
            break