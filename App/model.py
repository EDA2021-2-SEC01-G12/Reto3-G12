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
    expediente={"avistamientos":None,"fechas":None,"ciudades":None,"longitudes":None,"duracion":None}
    expediente["avistamientos"]=lt.newList("SINGLE_LINKED")
    expediente["fechas"]=mo.newMap(omaptype="RBT")
    expediente["ciudades"]=mp.newMap(numelements=803,maptype="CHAINING")
    expediente["longitudes"]=mo.newMap(omaptype="RBT")
    expediente["duraciones"]=mo.newMap(omaptype="RBT")
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

def addCity(expediente,avistamiento):
    ciudad=avistamiento["city"]
    if not mp.contains(expediente["ciudades"],ciudad):
        avistamientosCiudad=lt.newList("SINGLE_LINKED")
        lt.addLast(avistamientosCiudad,avistamiento)
        mp.put(expediente["ciudades"],ciudad,avistamientosCiudad)
    else:
        avistamientosCiudad=me.getValue(mp.get(expediente["ciudades"],ciudad))
        lt.addLast(avistamientosCiudad,avistamiento) 

def addLongitud(expediente,avistamiento):
    longitud=round(float(avistamiento['longitude']),2)
    if not mo.contains(expediente["longitudes"],longitud):
        avistamientos=lt.newList("SINGLE_LINKED")
        lt.addLast(avistamientos,avistamiento)
        mo.put(expediente["longitudes"],longitud,avistamientos)
    else:
        avistamientos=me.getValue(mo.get(expediente["longitudes"],longitud))
        lt.addLast(avistamientos,avistamiento)

def addDuration(expediente,avistamiento):
    duracion=float(avistamiento["duration (seconds)"])
    if not mo.contains(expediente["duraciones"],duracion):
        avistamientos=lt.newList("SINGLE_LINKED")
        lt.addLast(avistamientos,avistamiento)
        mo.put(expediente["duraciones"],duracion,avistamientos)
    else:
        avistamientos=me.getValue(mo.get(expediente["duraciones"],duracion))
        lt.addLast(avistamientos,avistamiento)

# Funciones para creacion de datos

# Funciones de consulta

def sightingsByCity(expediente,ciudad):
    ciudad=me.getValue(mp.get(expediente["ciudades"],ciudad))
    ciudad=ms.sort(ciudad,cmpDates)
    return ciudad

def avistamientosFechaMasAntigua(expediente):
    fechas=expediente["fechas"]
    fechaMasAntigua=mo.minKey(fechas)
    avistamientosFechaMasAntigua=me.getValue(mo.get(fechas,fechaMasAntigua))
    avis=lt.size(avistamientosFechaMasAntigua)
    return fechaMasAntigua,avis

def avistamientosPorDuracion(expediente,duracionMin,duracionMax):
    maxDuracion=mo.maxKey(expediente["duraciones"])
    numAvistamientosMaxKey=lt.size(me.getValue(mo.get(expediente["duraciones"],maxDuracion)))
    avisRango=mo.keys(expediente["duraciones"],duracionMin,duracionMax)
    listaAvistamientos=lt.newList("SINGLE_LINKED")
    for key in lt.iterator(avisRango):
        duracion=me.getValue(mo.get(expediente["duraciones"],key))
        for avis in lt.iterator(duracion):
            lt.addLast(listaAvistamientos,avis)
    listaAvistamientos=ms.sort(listaAvistamientos,cmpDuration)
    return maxDuracion,numAvistamientosMaxKey,listaAvistamientos

def avistamientosEnRango(expediente,fechaInicio,fechaFin):
    fechaInicio=(datetime.datetime.strptime(fechaInicio, '%Y-%m-%d')).date()
    fechaFin=(datetime.datetime.strptime(fechaFin, '%Y-%m-%d')).date()
    avistamientosFechas=lt.newList("SINGLE_LINKED")
    fechasEnRango=mo.keys(expediente["fechas"],fechaInicio,fechaFin)
    for date in lt.iterator(fechasEnRango):
        avistamientos=me.getValue(mo.get(expediente["fechas"],date))
        for sighting in lt.iterator(avistamientos):
            lt.addLast(avistamientosFechas,sighting)
    numAvistamientos=lt.size(avistamientosFechas)
    return numAvistamientos,avistamientosFechas

def avistamientosZona(expediente,longMin,longMax,latMin,latMax):
    longKeys=mo.keys(expediente["longitudes"],longMin,longMax)
    avistamientosLongLat=lt.newList("SINGLE_LINKED")
    for long in lt.iterator(longKeys):
        lista=me.getValue(mo.get(expediente["longitudes"],long))
        for avis in lt.iterator(lista):
            lat=float(avis["latitude"])
            lat=round(lat,2)
            if latMin<=lat<=latMax:
                lt.addLast(avistamientosLongLat,avis)
    num=lt.size(avistamientosLongLat)
    avistamientosLongLat=ms.sort(avistamientosLongLat,cmpLongLat)
    return avistamientosLongLat,num

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpDates(av1,av2):
    fecha1=int(av1["datetime"].split(" ")[0].replace(" ","").replace("-",""))
    fecha2=int(av2["datetime"].split(" ")[0].replace(" ","").replace("-",""))
    if fecha1<fecha2:
        return True
    else:
        return False

def cmpLongLat(avi1,avi2):
    lat1=round(float(avi1["latitude"]),2)
    lat2=round(float(avi2["latitude"]),2)
    if lat1<lat2:
        return True
    elif lat1>lat2:
        return False
    else:
        return avi1["longitude"]<avi2["longitude"]

def cmpDuration(avi1,avi2):
    duracion1=float(avi1["duration (seconds)"])
    duracion2=float(avi2["duration (seconds)"])
    ciudadPais1=avi1["city"]+" "+avi1["country"]
    ciudadPais2=avi2["city"]+" "+avi2["country"]
    if duracion1!=duracion2:
        return duracion1<duracion2
    else:
        return ciudadPais1<ciudadPais2

# Funciones de ordenamiento

def sortSightings(expediente):
    expediente["avistamientos"]=ms.sort(expediente["avistamientos"],cmpfunction=cmpDates)
    
