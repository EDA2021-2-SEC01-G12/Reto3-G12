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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

def createRecord():
    return model.createRecord()

# Funciones para la carga de datos

def addSightings(expediente):
    UFOSFile = cf.data_dir + "UFOS-utf8-small.csv"
    sightings = csv.DictReader(open(UFOSFile, encoding="utf-8"),delimiter=",")
    for avistamiento in sightings:
        model.addSightings(expediente, avistamiento)
        model.addCity(expediente,avistamiento)
        model.addLongitud(expediente,avistamiento)
        model.addDuration(expediente,avistamiento)
        model.addHoraMin(expediente,avistamiento)

# Funciones de ordenamiento

def sortSightings(expediente):
    model.sortSightings(expediente)

# Funciones de consulta sobre el catálogo

def sightingsByCity(expediente,ciudad):
    return model.sightingsByCity(expediente,ciudad)

def avistamientosFechaMasAntigua(expediente):
    return model.avistamientosFechaMasAntigua(expediente)

def avistamientosPorDuracion(expediente,duracionMin,duracionMax,requerimiento):
    return model.avistamientosPorDuracion(expediente,duracionMin,duracionMax,requerimiento)

def avistamientosEnRango(expediente,fechaInicio,fechaFin):
    return model.avistamientosEnRango(expediente,fechaInicio,fechaFin)

def avistamientosZona(expediente,longMin,longMax,latMin,latMax):
    return model.avistamientosZona(expediente,longMin,longMax,latMin,latMax)
