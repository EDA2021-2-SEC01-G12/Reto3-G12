"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import orderedmap as mo
from DISClib.ADT import list as lt
assert cf
import time


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def createRecord():
    return controller.createRecord()

def sortSightings(expediente):
    controller.sortSightings(expediente)

def sightingsByCity(expediente,ciudad):
    return controller.sightingsByCity(expediente,ciudad)

def avistamientosFechaMasAntigua(expediente):
    return controller.avistamientosFechaMasAntigua(expediente)

def avistamientosPorDuracion(expediente,duracionMin,duracionMax,requerimiento):
    return controller.avistamientosPorDuracion(expediente,duracionMin,duracionMax,requerimiento)

def avistamientosEnRango(expediente,fechaInicio,fechaFin):
    return controller.avistamientosEnRango(expediente,fechaInicio,fechaFin)

def avistamientosZona(expediente,longMin,longMax,latMin,latMax):
    return controller.avistamientosZona(expediente,longMin,longMax,latMin,latMax)

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar avistamientos ocurridos en una ciudad en especifico")
    print("3- Consultar avistamientos por su duracion")
    print("4- Consultar avistamientos por hora del dia en que sucedieron")
    print("5- Consultar avistamientos ocurridos dentro de un rango de fechas")
    print("6- Consultar avistamientos ocurridos en una zona geografica en especifico")
    print("7- Visualizar avistamientos ocurridos en una zona geografica en especifico")

def print10Sightings(expediente):
    avistamientos=expediente['avistamientos']
    i=1
    j=lt.size(avistamientos)-2
    avi=True
    print("Los cinco avistamientos mas antiguos y los cinco mas recientes registrados son: \n_________________________________________________________________________________________________________________________\n")
    while avi:
        if i!=4:
            avistamientoActual=lt.getElement(avistamientos,i)
            i+=1
        else:
            avistamientoActual=lt.getElement(avistamientos,j)
            j+=1
            if j==lt.size(avistamientos)+1:
                avi=False
        fechaHora,ciudad,pais,duracion,forma=avistamientoActual['datetime'],avistamientoActual['city'].title(),avistamientoActual['country'].upper(),avistamientoActual['duration (seconds)'],avistamientoActual['shape']
        if fechaHora=="":
            fechaHora="Desconocidas"
        if ciudad=="":
            ciudad="Desconocida"
        if pais=="":
            pais="Desconocido"
        if duracion=="":
            duracion="Desconocida"
        if forma=="":
            forma="Forma desconocida"
        print("- Fecha y hora del avistamiento: "+fechaHora+"\n- Pais: "+pais+"\n- Ciudad: "+ciudad+"\n- Duracion: "+duracion+" segundos\n- Forma: "+forma.title()+"\n_________________________________________________________________________________________________________________________\n")

def printSightings(lst,num1,num2,total):
    if lt.size(lst)>=total:
        i=num1
        j=lt.size(lst)-num2
        avi=True
        while avi:
            if i!=4:
                avistamientoActual=lt.getElement(lst,i)
                i+=1
            else:
                avistamientoActual=lt.getElement(lst,j)
                j+=1
                if j==lt.size(lst)+1:
                    avi=False
            fechaHora,ciudad,pais,duracion,forma,longitud,latitud=avistamientoActual['datetime'],avistamientoActual['city'].title(),avistamientoActual['country'].upper(),avistamientoActual['duration (seconds)'],avistamientoActual['shape'],avistamientoActual['longitude'],avistamientoActual['latitude']
            if fechaHora=="":
                fechaHora="Desconocidas"
            if ciudad=="":
                ciudad="Desconocida"
            if pais=="":
                pais="Desconocido"
            if duracion=="":
                duracion="Desconocida"
            if forma=="":
                forma="Forma desconocida"
            print("- Fecha y hora del avistamiento: "+fechaHora+"\n- Pais: "+pais+"\n- Ciudad: "+ciudad+"\n- Duracion: "+duracion+" segundos\n- Forma: "+forma.title()+"\n- Longitud: "+str(longitud)+"\n- Latitud: "+str(latitud)+"\n_________________________________________________________________________________________________________________________\n")
    else:
        for avis in lt.iterator(lst):
            fechaHora,ciudad,pais,duracion,forma,longitud,latitud=avis['datetime'],avis['city'].title(),avis['country'].upper(),avis['duration (seconds)'],avis['shape'],avis['longitude'],avis['latitude']
            if fechaHora=="":
                fechaHora="Desconocidas"
            if ciudad=="":
                ciudad="Desconocida"
            if pais=="":
                pais="Desconocido"
            if duracion=="":
                duracion="Desconocida"
            if forma=="":
                forma="Forma desconocida"
            print("- Fecha y hora del avistamiento: "+fechaHora+"\n- Pais: "+pais+"\n- Ciudad: "+ciudad+"\n- Duracion: "+duracion+" segundos\n- Forma: "+forma.title()+"\n- Longitud: "+str(longitud)+"\n- Latitud: "+str(latitud)+"\n_________________________________________________________________________________________________________________________\n")

expediente = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if inputs == "1":
        print("Cargando información de los archivos ....")
        start_time1 = time.process_time()
        expediente=createRecord()
        controller.addSightings(expediente)
        sortSightings(expediente)
        stop_time1= time.process_time()
        timeSort1= (stop_time1-start_time1)*1000
        print ("\nAvistamientos cargados: "+str(lt.size(expediente["avistamientos"]))+"\n")
        print10Sightings(expediente)
        print(str(timeSort1)+'milisegundos')
    elif inputs == "2":
        ciudad=input("Ingrese el nombre de la ciudad a consultar: \n")
        start_time2 = time.process_time()
        exp=sightingsByCity(expediente,ciudad)
        stop_time2= time.process_time()
        timeSort2= (stop_time2-start_time2)*1000
        print("\nAltura del arbol: "+str(mo.height(expediente["fechas"])))
        print("Elementos en el arbol: "+str(mo.size(expediente["fechas"]))+"\n")
        print("Se han registrado "+str(lt.size(exp))+" avistamientos en "+ciudad.title())
        if lt.size(exp)>=6:
            print("\nLos tres avistamientos mas antiguos y los tres mas recientes registrados en esta ciudad son: \n_________________________________________________________________________________________________________________________\n")
        else:
            print("_________________________________________________________________________________________________________________________\n")
        printSightings(exp,1,2,6)
        print(str(timeSort2)+'milisegundos')
    elif inputs == "3":
        duracionMin=float(input("Ingrese la duracion minima en segundos para la busqueda:\n"))
        duracionMax=float(input("Ingrese la duracion maxima en segundos para la busqueda:\n"))
        start_time3 = time.process_time()
        avistamientos=avistamientosPorDuracion(expediente,duracionMin,duracionMax,"2")
        stop_time3= time.process_time()
        timeSort3= (stop_time3-start_time3)*1000
        print("\nLa mayor duracion registrada es de "+str(avistamientos[0])+" segundos con "+str(avistamientos[1])+" avistamiento(s)")
        if lt.size(avistamientos[2])>=6:
            print("\nLos tres avistamientos mas antiguos y los tres mas recientes registrados en esta ciudad son: \n_________________________________________________________________________________________________________________________\n")
        else:
            print("_________________________________________________________________________________________________________________________\n")
        printSightings(avistamientos[2],1,2,6)
        print(str(timeSort3)+'milisegundos')
    elif inputs == "4":
        horaMin=input("Ingrese el tiempo minimo (en formato HH:MM) para la busqueda en formato:\n")
        horaMax=input("Ingrese el tiempo maximo (en formato HH:MM) para la busqueda en formato:\n")
        start_time4 = time.process_time()
        avistamientos=avistamientosPorDuracion(expediente,horaMin,horaMax,"3")
        stop_time4= time.process_time()
        timeSort4= (stop_time4-start_time4)*1000
        print("\nLa mayor duracion registrada es de "+str(avistamientos[0])+" segundos con "+str(avistamientos[1])+" avistamiento(s)")
        print("\nEl total de avistamientos ocurridos entre "+horaMin+" y "+horaMax+" son "+str(lt.size(avistamientos[2])))
        if lt.size(avistamientos[2])>=6:
            print("\nLos tres avistamientos mas antiguos y los tres mas recientes registrados en esta ciudad son: \n_________________________________________________________________________________________________________________________\n")
        else:
            print("_________________________________________________________________________________________________________________________\n")
        printSightings(avistamientos[2],1,2,6)
        print(str(timeSort4)+'milisegundos')
    elif inputs == "5":
        fecha=avistamientosFechaMasAntigua(expediente)
        print("\nLa fecha mas antigua con avistamientos registrados es ",fecha[0]," donde hubo "+str(fecha[1])+" avistamiento(s)\n")
        anioInicio,mesInicio,diaInicio,anioFin,mesFin,diaFin=True,True,True,True,True,True
        print("Ingrese el año inicial en formato de 4 dígitos:")
        anio1=input("")
        while anioInicio:
            if len(anio1)!=4:
                print("El número ingresado tiene un formato invalido")
                anio1=input("")
            else:
                anioInicio=False
        print("Ingrese el mes inicial en formato de 2 dígitos:")
        mes1=input("")
        while mesInicio:
            if len(mes1)!=2:
                print("El número ingresado tiene un formato invalido")
                mes1=input("")
            else:
                mesInicio=False
        print("Ingrese el dia inicial en formato de 2 dígitos:")
        dia1=input("")
        while diaInicio:
            if len(dia1)!=2:
                print("El número ingresado tiene un formato invalido")
                dia1=input("")
            else:
                diaInicio=False
        print("Ingrese el año final en formato de 4 dígitos:")
        anio2=input("")
        while anioFin:
            if len(anio2)!=4:
                print("El número ingresado tiene un formato invalido")
                anio2=input("")
            else:
                anioFin=False
        print("Ingrese el mes final en formato de 2 dígitos:")
        mes2=input("")
        while mesFin:
            if len(mes2)!=2:
                print("El número ingresado tiene un formato invalido")
                mes2=input("")
            else:
                mesFin=False
        print("Ingrese el dia inicial en formato de 2 dígitos:")
        dia2=input("")
        while diaFin:
            if len(dia2)!=2:
                print("El número ingresado tiene un formato invalido")
                dia2=input("")
            else:
                diaFin=False
        fechaInicio=anio1+"-"+mes1+"-"+dia1
        fechaFin=anio2+"-"+mes2+"-"+dia2
        start_time5 = time.process_time()
        avistamientos=avistamientosEnRango(expediente,fechaInicio,fechaFin)
        stop_time5= time.process_time()
        timeSort5= (stop_time5-start_time5)*1000
        print("\nSe tiene registro de "+str(avistamientos[0])+" avistamientos entre "+fechaInicio+" y "+fechaFin)
        if avistamientos[0]>=6:
            print("\nLos tres avistamientos mas antiguos y los tres mas recientes registrados entre estas fechas son: \n_________________________________________________________________________________________________________________________\n")
        else:
            print("_________________________________________________________________________________________________________________________\n")
        printSightings(avistamientos[1],1,2,6)
        print(str(timeSort5)+'milisegundos')
    elif inputs == "6":
        longMin=float(input("Ingrese la longitud minima para la busqueda:\n"))
        longMax=float(input("Ingrese la longitud maxima para la busqueda:\n"))
        latMin=float(input("Ingrese la latitud minima para la busqueda:\n"))
        latMax=float(input("Ingrese la latitud maxima para la busqueda:\n"))
        start_time6 = time.process_time()
        avistamientosZoneGeo=avistamientosZona(expediente,longMin,longMax,latMin,latMax)
        stop_time6= time.process_time()
        timeSort6= (stop_time6-start_time6)*1000
        avis=avistamientosZoneGeo[0]
        numero=avistamientosZoneGeo[1]
        print("\nSe tiene registro de "+str(numero)+" avistamientos entre las latitudes "+str(longMin)+" y "+str(longMax)+" y las latitudes "+str(latMin)+" y "+str(latMax))
        if numero>=10:
            print("\nLos primeros y ultimos cinco avistamientos registrados en esta zona son: \n_________________________________________________________________________________________________________________________\n")
        else:
            print("_________________________________________________________________________________________________________________________\n")
        printSightings(avis,1,9,10)
        print(str(timeSort6)+'milisegundos')
    elif inputs == "7":
        pass
    elif inputs == "0":
        sys.exit(0)
    else:
        print("\nOpcion invalida\n")
sys.exit(0)


#preguntas pal profe
