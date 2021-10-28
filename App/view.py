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

def avistamientosEnRango(expediente,fechaInicio,fechaFin):
    return controller.avistamientosEnRango(expediente,fechaInicio,fechaFin)

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

def printSightingsByCity(lstCiudad):
    if lt.size(lstCiudad)>=6:
        i=1
        j=lt.size(lstCiudad)-2
        avi=True
        print("\nLos tres avistamientos mas antiguos y los tres mas recientes registrados en esa ciudad son: \n_________________________________________________________________________________________________________________________\n")
        while avi:
            if i!=4:
                avistamientoActual=lt.getElement(lstCiudad,i)
                i+=1
            else:
                avistamientoActual=lt.getElement(lstCiudad,j)
                j+=1
                if j==lt.size(lstCiudad)+1:
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
    else:
        print("_________________________________________________________________________________________________________________________\n")
        for avis in lt.iterator(lstCiudad):
            fechaHora,ciudad,pais,duracion,forma=avis['datetime'],avis['city'].title(),avis['country'].upper(),avis['duration (seconds)'],avis['shape']
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

expediente = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if inputs == "1":
        print("Cargando información de los archivos ....")
        expediente=createRecord()
        controller.addSightings(expediente)
        sortSightings(expediente)
        print ("\nAvistamientos cargados: "+str(lt.size(expediente["avistamientos"]))+"\n")
        print10Sightings(expediente)
    elif inputs == "2":
        print("\nAltura del arbol: "+str(mo.height(expediente["fechas"])))
        print("Elementos en el arbol: "+str(mo.size(expediente["fechas"]))+"\n")
        ciudad=input("Ingrese el nombre de la ciudad a consultar: \n")
        exp=sightingsByCity(expediente,ciudad)
        print("\nSe han registrado "+str(lt.size(exp))+" avistamientos en "+ciudad.title())
        printSightingsByCity(exp)
    elif inputs == "3":
        pass
    elif inputs == "4":
        pass
    elif inputs == "5":
        fecha=avistamientosFechaMasAntigua(expediente)
        print("La fecha mas antigua con avistamientos registrados es ",fecha[0]," donde hubo "+str(fecha[1])+" avistamiento(s)")
        fechaInicio=input("Ingrese la fecha incial para la consulta:\n")
        fechaFin=input("Ingrese la fecha final para la consulta:\n")
        avistamientos=avistamientosEnRango(expediente,fechaInicio,fechaFin)
    elif inputs == "6":
        pass
    elif inputs == "7":
        pass
    elif inputs == "0":
        sys.exit(0)
    else:
        print("\nOpcion invalida\n")
sys.exit(0)


#preguntas pal profe

'''
Toca imprimir tal cual nos dice el ejemplo? o nos apegamos a lo que dice el enunciado (ej: req 1 aparece 
el top 5 y req 4: pide la ultima fecha y su numero de avistamientos, pero en el ejemplo aparecen las ultimas
5 fechas)


'''