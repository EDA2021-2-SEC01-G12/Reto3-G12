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
    print("Los primeros y últimos cinco avistamientos registrados son: \n_________________________________________________________________________________________________________________________\n")
    while avi:
        if i!=4:
            avistamientoActual=lt.getElement(avistamientos,i)
            i+=1
        else:
            avistamientoActual=lt.getElement(avistamientos,j)
            j+=1
            if j==lt.size(avistamientos)+1:
                avi=False
        fechaHora,ciudad,pais,duracion,forma=avistamientoActual['datetime'],avistamientoActual['city'],avistamientoActual['country'].upper(),avistamientoActual['duration (seconds)'],avistamientoActual['shape']
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
        print("- Fecha y hora del avistamiento: "+fechaHora+"\n- Pais: "+pais+"\n- Ciudad: "+ciudad+"\n- Duracion: "+duracion+"\n- Forma: "+forma+"\n_________________________________________________________________________________________________________________________\n")

expediente = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        expediente=createRecord()
        controller.addSightings(expediente)
        sortSightings(expediente)
        print ("\nAvistamientos cargados: "+str(lt.size(expediente["avistamientos"]))+"\n")
        print10Sightings(expediente)
        #print(lt.firstElement(expediente["avistamientos"]))
        #print(lt.lastElement(expediente["avistamientos"]))
    elif int(inputs[0]) == 2:
        print("\nAltura del arbol: "+str(mo.height(expediente["fechas"])))
        print("Elementos en el arbol: "+str(mo.size(expediente["fechas"]))+"\n")
    elif int(inputs[0]) == 3:
        #print(mo.minKey(expediente['fechas']))
        #print(str(mo.maxKey(expediente['fechas']))+"\n")
        pass
    elif int(inputs[0]) == 4:
        pass
    elif int(inputs[0]) == 5:
        pass
    elif int(inputs[0]) == 6:
        pass
    elif int(inputs[0]) == 7:
        pass
    else:
        sys.exit(0)
sys.exit(0)
