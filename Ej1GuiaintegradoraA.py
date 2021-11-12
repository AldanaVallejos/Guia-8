#***********************************************************
# Fecha: 22/10/2021
# Autor: Aldana Vallejos
# Guia N7
#***********************************************************
# EJERCICIO 1: Escribir funciones que resuelvan los siguientes problemas: 
# a) Dado un año indicar si es bisiesto. Nota: un año es bisiesto si es un número divisible por 4, pero no si es divisible por 100, excepto que también sea divisible por 400. 
# a) LISTO
# b) Dado un mes y un año, devolver la cantidad de días correspondientes. 
# c) Dada una fecha (día, mes, año), indicar si es válida o no. 
# d) Dada una fecha, indicar los días que faltan hasta fin de mes. 
# e) Dada una fecha, indicar los días que faltan hasta fin de año. 
# f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
# g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días
# Nota: en todos los casos, invocar las funciones escritas previamente cuando sea posible.

#***********************************************************
#                    D I S E Ñ O
#***********************************************************
# Declaración de variables
from datetime import date
dia=0
mes=0
año=0
opcion=""
dia1=0
dia2=0
mes1=0
mes2=0
año1=0
año2=0
while True:
    #********************************************** CONSIGNA A) ********************************************
    def bisiesto (año): #FUNCION PARA LA CONSIGNA a)
        while año<=0: #INGRESO DE DATOS Y VALIDACIONES
            try:
                año=int(input("Ingrese un año para saber si es bisiesto: "))
                if año<=0:
                    print("Error. Ingrese un valor correcto")
            except ValueError:
                print("Error. Ingrese números")
        
        if año%4==0: #Salidas por pantalla
            print("El año ingresado ES bisiesto")
        elif año%100==0 and año%400==0:
                print("El año ingresado ES bisiesto")
        else:
            print("El año ingresado NO es bisiesto")
    
    #********************************************** CONSIGNA B) ********************************************
    def cant_dias (mes,año):
        dias=["28 días","29 días" ,"30 días" ,"31 días"]
        mes=0

        while año<=0 or mes<=0:
            try:
                mes=int(input("Ingrese el mes: ")) #Ingreso de datos
                if mes<=0:
                    print("Error. Ingrese un valor válido")
                else:
                    while mes>0:
                        año=int(input("Ingrese el año: "))
                        if año <=0:
                            print("Error. Ingrese un valor válido")
                        else:
                            break
            except ValueError:
                print("Error. Ingrese números")

        if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12: #Caso enero, marzo, mayo, julio, agosto, octubre y diciembre
            print(dias[3]) #Salida por pantalla
        elif mes==4 or mes==6 or mes==9 or mes==11: #caso abril, junio, septiembre y noviembre
                print(dias[2]) #Salida por pantalla
        elif mes==2 and año%4==0:
            print(dias[1]) #Salida por pantalla
        else:
            print(dias[0]) #Salida por pantalla

    #********************************************** CONSIGNA C) ********************************************
    def fecha(dia,mes,año):
        dia=0
        mes=0
        año=0
        try: #Validaciones
            dia=int(input("Ingrese el día: ")) #Ingreso de datos
            mes=int(input("Ingrese el mes: "))
            año=int(input("Ingrese el año: "))
        except ValueError:
            print("Error. Ingrese números")
            dia=int(input("Ingrese el día: "))
            mes=int(input("Ingrese el mes: "))
            año=int(input("Ingrese el año: "))

        if año>2021:
            print("No es una fecha válida.")
        elif mes<1 or mes>12:
            print("No es una fecha válida.")
        elif dia<1 or dia>31:
            print("No es una fecha válida.")
        elif mes==4 or mes==6 or mes==9 or mes==11:
                if dia<1 or dia>30:
                    print("No es una fecha válida.") #Salidas por pantalla
                else:
                    print("Es una fecha válida.")                 
        elif mes==2 and año%4!=0:
                if dia<1 or dia>28:
                    print("No es una fecha válida.")
                else:
                    print("Es una fecha válida.")
        elif mes==2 and año%4==0:
                if dia<1 or dia>29:
                    print("No es una fecha válida.")
                else:
                    print("Es una fecha válida.")
        else:
            print("Es una fecha válida.")
    
    #****************************************** CONSIGNA D) ************************************************
    def diasfindemes (dia,mes,año):
        #Declaración de variables
        dia=0
        mes=0
        año=0
        dias_que_faltan=0
        while dia<=0 or mes<=0: #Validaciones
            try:
                dia=int(input("Ingrese el dia: "))
                if dia<=0:
                    print("Error. dia inválido")
                else:
                    mes=int(input("Ingrese el mes: "))
                    if mes<=0:
                        print("Error. mes inválido")
                        mes=int(input("Ingrese el mes: "))
            except ValueError:
                print("Error. Ingrese números")
        
        while año<=0 or año>2021:
            try:
                año=int(input("Ingrese el año: "))
                if año<=0 or año>2021:
                    print("Error. Año inválido")
            except ValueError:
                print("Error. Ingrese números")
        
        #Salidas por pantalla
        if mes==2:
            dias_que_faltan=28-dia
            print(f"Faltan {dias_que_faltan} días hasta fin de mes")
        elif mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
            dias_que_faltan=31-dia
            print(f"Faltan {dias_que_faltan} días hasta fin de mes")
        else:
            dias_que_faltan=30-dia
            print(f"Faltan {dias_que_faltan} días hasta fin de mes")
    
    #****************************************** CONSIGNA E) ************************************************
    def diasfindeano(fecha):
        #Declaración de variables
        fecha=0
        dias_que_faltan=0
        from datetime import datetime
        fecha=input("Ingrese una fecha en formato dia/mes/año: ")
        fechainicial=datetime.strptime(fecha,"%d/%m/%Y")
        fin_ano=datetime.strptime("31/12/2021", "%d/%m/%Y")
        diferencia = fin_ano - fechainicial
        print("Faltan", diferencia.days, "días hasta fin de año") #Salida por pantalla
    
    #****************************************** CONSIGNA F) ************************************************
    def diastranscurridos(fecha):
        #Declaración de variables
        dia=0
        mes=0
        año=0
        diastranscurridos=0
        from datetime import datetime
        
        while año<=0 or año>2021:
            año=int(input("Ingrese el año: "))
            if año<=0 or año>2021:
                print("Error. Ingrese un año válido") #Validaciones
        
        while mes<=0 or mes>12:
            mes=int(input("Ingrese el mes: "))
            if mes<=0 or mes>12:
                print("Error. Ingrese un mes válido")
        
        while dia<=0 or dia>31:
            dia=int(input("Ingrese un dia: "))
            if dia<=0 or dia>31:
                print("Error. Ingrese un dia correcto")
            elif mes==4 or mes==6 or mes==9 or mes==11:
                if dia<=0 or dia>30:
                    print("Error. Ingrese un dia válido")
                else:
                    break
            elif mes==2 and año%4!=0:
                if dia<=0 or dia>28:
                    print("Error. Ingrese un día válido")
                else:
                    break
            elif mes==2 and año%4==0:
                if dia<=0 or dia>29:
                    print("Error. Ingrese un día válido")
            else:
                break

        fechaingresada=date(año, mes, dia)
        fechainicial=date(año, 1, 1)
        delta = fechainicial - fechaingresada
        print("Transcurrieron", abs(delta.days), "dias hasta la fecha.") #Salida por pantalla
    
    #****************************************** CONSIGNA G) ************************************************
    def tiempotranscurrido (dia1, mes1, año1, dia2, mes2, año2):
        try: #validación
            año1=int(input("Ingrese el año de la primera fecha: ")) #Ingreso de datos
            mes1=int(input("Ingrese el mes de la primera fecha: "))
            dia1=int(input("Ingrese el dia de la primera fecha: "))
            año2=int(input("Inserte el año de la segunda fecha: "))
            mes2=int(input("Inserte el mes de la segunda fecha: "))
            dia2=int(input("Inserte el dia de la segunda fecha: "))
        except ValueError:
            print("Error. Ingrese números")
        #Declaracion de variables
        resultado=0
        añobisiesto=año1//4
        añobisiesto2=año1//400
        año_total=año2-año1
        mes_total=mes2-mes1
        dia_total=0
        while mes_total<0:
            año_total-=1
            mes_total+=12
            dia_total=dia2-dia1
            while dia_total<0:
                mes_total-=1
                if añobisiesto==0 or añobisiesto2==0:
                    if mes==2:
                        resultado+=29
                else:
                    if mes==2:
                        resultado+=28
                if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
                    resultado+=31
                elif mes==4 or mes==6 or mes==9 or mes==11:
                    resultado+=30
        print(f"El tiempo transcurrido entre ambas fechas ingresadas fue de: {año_total} años, {mes_total} meses Y {dia_total} dias.") #Salida por pantalla
    
    # MENÚ
    print("""*********MENÚ************
    a) Dado un año indicar si es bisiesto.
    b) Dado un mes y un año, devolver la cantidad de días correspondientes. 
    c) Dada una fecha (día, mes, año), indicar si es válida o no. 
    d) Dada una fecha, indicar los días que faltan hasta fin de mes. 
    e) Dada una fecha, indicar los días que faltan hasta fin de año. 
    f) Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
    g) Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.
    h) Salir.""")
    opcion=input("Ingrese una opción: ") #Ingreso de dato

    if opcion.lower()!="a" and opcion.lower()!="b" and opcion.lower()!="c" and opcion.lower()!="d" and opcion.lower()!="e" and opcion.lower()!="f" and opcion.lower()!="g" and opcion.lower()!="h":
        print("Error. el caracter ingresado no corresponde.") #Validación
    elif opcion.lower()=="h": #Caso salir
        print("Saliendo.")
        break
    elif opcion.lower()=="a": #Caso Dado un año indicar si es bisiesto.
        bisiesto(año)
    elif opcion.lower()=="b": #Caso Dado un mes y un año, devolver la cantidad de días correspondientes. 
        cant_dias(mes,año)
    elif opcion.lower()=="c": #Caso Dada una fecha (día, mes, año), indicar si es válida o no. 
        fecha(dia,mes,año)
    elif opcion.lower()=="d": #Caso Dada una fecha, indicar los días que faltan hasta fin de mes. 
        diasfindemes(dia,mes,año)
    elif opcion.lower()=="e": #Caso Dada una fecha, indicar los días que faltan hasta fin de año. 
        diasfindeano(fecha)
    elif opcion.lower()=="f": #Caso Dada una fecha, indicar la cantidad de días transcurridos en ese año hasta esa fecha.
        diastranscurridos(fecha)
    elif opcion.lower()=="g": #Caso Dadas dos fechas (día1, mes1, año1, día2, mes2, año2), indicar el tiempo transcurrido entre ambas, en años, meses y días.
        tiempotranscurrido(dia1, mes1, año1, dia2, mes2, año2)