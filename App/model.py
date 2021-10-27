"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as mo
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as ms
import datetime
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def createRecord():
    expediente={"avistamientos":None,"fechas":None}
    expediente["avistamientos"]=lt.newList("SINGLE_LINKED")
    expediente["fechas"]=mo.newMap(omaptype="RBT")
    return expediente

# Funciones para agregar informacion al catalogo

def addSightings(expediente,avistamiento):
    av=avistamiento["datetime"]
    fecha=datetime.datetime.strptime(av, '%Y-%m-%d %H:%M:%S')
    if not mo.contains(expediente["fechas"],fecha.date()):
        avistamientosFecha=lt.newList("SINGLE_LINKED")
        lt.addLast(avistamientosFecha,avistamiento)
        mo.put(expediente["fechas"],fecha.date(),avistamientosFecha)
    else:
        avistamientosFecha=me.getValue(mo.get(expediente["fechas"],fecha.date()))
        lt.addLast(avistamientosFecha,avistamiento)
    lt.addLast(expediente["avistamientos"],avistamiento)    

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpDates(av1,av2):
    fecha1=int(av1["datetime"].split(" ")[0].replace(" ","").replace("-",""))
    fecha2=int(av2["datetime"].split(" ")[0].replace(" ","").replace("-",""))
    if fecha1<fecha2:
        return True
    else:
        return False

# Funciones de ordenamiento

def sortSightings(expediente):
    expediente["avistamientos"]=ms.sort(expediente["avistamientos"],cmpfunction=cmpDates)
    
